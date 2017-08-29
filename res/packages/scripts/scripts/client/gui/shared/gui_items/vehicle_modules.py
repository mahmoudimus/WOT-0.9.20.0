# 2017.08.29 21:49:39 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/vehicle_modules.py
import BigWorld
from constants import SHELL_TYPES
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.shared.items_parameters.params_cache import g_paramsCache
import nations
from helpers import i18n
from items import vehicles as veh_core
from gui.shared.gui_items.fitting_item import FittingItem, ICONS_MASK
from gui.shared.utils import GUN_CLIP, GUN_CAN_BE_CLIP
from gui.shared.money import Currency
MODULE_TYPES_ORDER = ('vehicleGun', 'vehicleTurret', 'vehicleEngine', 'vehicleChassis', 'vehicleRadio', 'vehicleFuelTank')
MODULE_TYPES_ORDER_INDICES = dict(((n, i) for i, n in enumerate(MODULE_TYPES_ORDER)))
SHELL_TYPES_ORDER = (SHELL_TYPES.ARMOR_PIERCING,
 SHELL_TYPES.ARMOR_PIERCING_CR,
 SHELL_TYPES.HOLLOW_CHARGE,
 SHELL_TYPES.HIGH_EXPLOSIVE)
SHELL_TYPES_ORDER_INDICES = dict(((n, i) for i, n in enumerate(SHELL_TYPES_ORDER)))

class VehicleModule(FittingItem):
    __slots__ = ('_vehicleModuleDescriptor',)

    def __init__(self, intCompactDescr, proxy = None, descriptor = None):
        super(VehicleModule, self).__init__(intCompactDescr, proxy)
        self._vehicleModuleDescriptor = descriptor

    @property
    def icon(self):
        return ''

    @property
    def descriptor(self):
        if self._vehicleModuleDescriptor is not None:
            return self._vehicleModuleDescriptor
        else:
            return super(VehicleModule, self).descriptor

    def _sortByType(self, other):
        return MODULE_TYPES_ORDER_INDICES[self.itemTypeName] - MODULE_TYPES_ORDER_INDICES[other.itemTypeName]

    def getGUIEmblemID(self):
        return self.itemTypeName


class VehicleChassis(VehicleModule):
    __slots__ = ()

    def isInstalled(self, vehicle, slotIdx = None):
        return self.intCD == vehicle.chassis.intCD

    def mayInstall(self, vehicle, slotIdx = None):
        installPossible, reason = FittingItem.mayInstall(self, vehicle, slotIdx)
        if not installPossible and reason == 'too heavy':
            return (False, 'too heavy chassis')
        return (installPossible, reason)

    def getInstalledVehicles(self, vehicles):
        result = set()
        for vehicle in vehicles:
            if self.intCD == vehicle.chassis.intCD:
                result.add(vehicle)

        return result

    def isHydraulicChassis(self):
        return g_paramsCache.isChassisHydraulic(self.intCD)

    @property
    def icon(self):
        return RES_ICONS.MAPS_ICONS_MODULES_CHASSIS


class VehicleTurret(VehicleModule):
    __slots__ = ()

    def isInstalled(self, vehicle, slotIdx = None):
        return self.intCD == vehicle.turret.intCD

    def mayInstall(self, vehicle, slotIdx = None, gunCD = 0):
        installPossible, reason = vehicle.descriptor.mayInstallTurret(self.intCD, gunCD)
        if not installPossible and reason == 'not for this vehicle type':
            return (False, 'need gun')
        return (installPossible, reason)

    def getInstalledVehicles(self, vehicles):
        result = set()
        for vehicle in vehicles:
            if self.intCD == vehicle.turret.intCD:
                result.add(vehicle)

        return result

    @property
    def icon(self):
        return RES_ICONS.MAPS_ICONS_MODULES_TOWER


class VehicleGun(VehicleModule):
    __slots__ = ('_defaultAmmo', '_maxAmmo')

    def __init__(self, intCompactDescr, proxy = None, descriptor = None):
        super(VehicleGun, self).__init__(intCompactDescr, proxy, descriptor)
        self._defaultAmmo = self._getDefaultAmmo(proxy)
        self._maxAmmo = self._getMaxAmmo(proxy)

    def isInstalled(self, vehicle, slotIdx = None):
        return self.intCD == vehicle.gun.intCD

    def mayInstall(self, vehicle, slotIdx = None):
        installPossible, reason = FittingItem.mayInstall(self, vehicle)
        if not installPossible and reason == 'not for current vehicle':
            return (False, 'need turret')
        return (installPossible, reason)

    def getReloadingType(self, vehicleDescr = None):
        return g_paramsCache.getGunReloadingSystemType(self.intCD, vehicleDescr.type.compactDescr if vehicleDescr is not None else None)

    def isClipGun(self, vehicleDescr = None):
        typeToCheck = GUN_CLIP if vehicleDescr is not None else GUN_CAN_BE_CLIP
        return self.getReloadingType(vehicleDescr) == typeToCheck

    def _getDefaultAmmo(self, proxy):
        result = []
        shells = veh_core.getDefaultAmmoForGun(self.descriptor)
        for i in range(0, len(shells), 2):
            result.append(Shell(shells[i], defaultCount=shells[i + 1], proxy=proxy))

        return result

    def _getMaxAmmo(self, proxy):
        return self.descriptor.maxAmmo

    def getInstalledVehicles(self, vehicles):
        result = set()
        for vehicle in vehicles:
            if self.intCD == vehicle.gun.intCD:
                result.add(vehicle)

        return result

    @property
    def defaultAmmo(self):
        return self._defaultAmmo

    @property
    def maxAmmo(self):
        return self._maxAmmo

    @property
    def icon(self):
        return RES_ICONS.MAPS_ICONS_MODULES_GUN


class VehicleEngine(VehicleModule):
    __slots__ = ()

    def isInstalled(self, vehicle, slotIdx = None):
        return self.intCD == vehicle.engine.intCD

    def getInstalledVehicles(self, vehicles):
        result = set()
        for vehicle in vehicles:
            if self.intCD == vehicle.engine.intCD:
                result.add(vehicle)

        return result

    def getConflictedEquipments(self, vehicle):
        conflictEqs = list()
        oldModuleId = vehicle.engine.intCD
        vehicle.descriptor.installComponent(self.intCD)
        for eq in vehicle.equipment.regularConsumables.getInstalledItems():
            installPossible, reason = eq.descriptor.checkCompatibilityWithVehicle(vehicle.descriptor)
            if not installPossible:
                conflictEqs.append(eq)

        vehicle.descriptor.installComponent(oldModuleId)
        return conflictEqs

    @property
    def icon(self):
        return RES_ICONS.MAPS_ICONS_MODULES_ENGINE


class VehicleFuelTank(VehicleModule):
    __slots__ = ()

    def isInstalled(self, vehicle, slotIdx = None):
        return self.intCD == vehicle.fuelTank.intCD

    def getInstalledVehicles(self, vehicles):
        result = set()
        for vehicle in vehicles:
            if self.intCD == vehicle.fuelTank.intCD:
                result.add(vehicle)

        return result


class VehicleRadio(VehicleModule):
    __slots__ = ()

    def isInstalled(self, vehicle, slotIdx = None):
        return self.intCD == vehicle.radio.intCD

    def getInstalledVehicles(self, vehicles):
        result = set()
        for vehicle in vehicles:
            if self.intCD == vehicle.radio.intCD:
                result.add(vehicle)

        return result

    @property
    def icon(self):
        return RES_ICONS.MAPS_ICONS_MODULES_RADIO


class Shell(FittingItem):
    __slots__ = ('_count', '_defaultCount')

    def __init__(self, intCompactDescr, count = 0, defaultCount = 0, proxy = None, isBoughtForCredits = False):
        """
        Ctor.
        
        @param intCompactDescr: item int compact descriptor
        @param count: count of shells in ammo bay
        @param defaultCount: count default shells in ammo bay
        @param proxy: instance of ItemsRequester
        """
        FittingItem.__init__(self, intCompactDescr, proxy, isBoughtForCredits)
        self._count = count
        self._defaultCount = defaultCount

    @property
    def level(self):
        """Return 0 because shell has no level."""
        return 0

    def _getAltPrice(self, buyPrice, proxy):
        """
        Returns an alternative price (right now in Currency.CREDITS) based on the original buy price and shells
        gold-credits exchange rate defined in the shop.
        
        @param buyPrice: buy price in Money
        @param proxy: shop stats proxy, see IShopCommonStats
        @return: alternative price in Money (right now in credits)
        """
        if Currency.GOLD in buyPrice:
            return buyPrice.exchange(Currency.GOLD, Currency.CREDITS, proxy.exchangeRateForShellsAndEqs)
        return super(Shell, self)._getAltPrice(buyPrice, proxy)

    def _getFormatLongUserName(self, kind):
        if self.nationID == nations.INDICES['germany']:
            caliber = float(self.descriptor.caliber) / 10
            dimension = i18n.makeString('#item_types:shell/dimension/sm')
        elif self.nationID == nations.INDICES['usa']:
            caliber = float(self.descriptor.caliber) / 25.4
            dimension = i18n.makeString('#item_types:shell/dimension/inch')
        else:
            caliber = self.descriptor.caliber
            dimension = i18n.makeString('#item_types:shell/dimension/mm')
        return i18n.makeString('#item_types:shell/name') % {'kind': i18n.makeString('#item_types:shell/%s/%s' % (kind, self.descriptor.kind)),
         'name': self.userName,
         'caliber': BigWorld.wg_getNiceNumberFormat(caliber),
         'dimension': dimension}

    @property
    def count(self):
        return self._count

    @property
    def defaultCount(self):
        return self._defaultCount

    @property
    def type(self):
        """ Returns shells type string (`HOLLOW_CHARGE` etc.). """
        return self.descriptor.kind

    @property
    def longUserName(self):
        return self._getFormatLongUserName('kinds')

    @property
    def longUserNameAbbr(self):
        return self._getFormatLongUserName('kindsAbbreviation')

    @property
    def icon(self):
        return ICONS_MASK[:-4] % {'type': self.itemTypeName,
         'subtype': '',
         'unicName': self.descriptor.icon[0]}

    def getGUIEmblemID(self):
        return self.type

    @property
    def defaultLayoutValue(self):
        return (self.intCD if not self.isBoughtForAltPrice else -self.intCD, self.defaultCount)

    def isInstalled(self, vehicle, slotIdx = None):
        for shell in vehicle.shells:
            if self.intCD == shell.intCD:
                return True

        return super(Shell, self).isInstalled(vehicle, slotIdx)

    def _sortByType(self, other):
        return SHELL_TYPES_ORDER_INDICES[self.type] - SHELL_TYPES_ORDER_INDICES[other.type]
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\vehicle_modules.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:49:39 St�edn� Evropa (letn� �as)
