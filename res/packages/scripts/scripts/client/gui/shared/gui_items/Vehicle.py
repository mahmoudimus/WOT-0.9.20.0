# 2017.08.29 21:49:37 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/Vehicle.py
from itertools import izip
from operator import itemgetter
import BigWorld
import math
import constants
from AccountCommands import LOCK_REASON, VEHICLE_SETTINGS_FLAG
from account_shared import LayoutIterator, getCustomizedVehCompDescr
from constants import WIN_XP_FACTOR_MODE
from gui import makeHtmlString
from gui.Scaleform.locale.ITEM_TYPES import ITEM_TYPES
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.prb_control import prb_getters
from gui.prb_control.settings import PREBATTLE_SETTING_NAME
from gui.shared.economics import calcRentPackages, getActionPrc, calcVehicleRestorePrice
from gui.shared.formatters import text_styles
from gui.shared.gui_items import CLAN_LOCK, GUI_ITEM_TYPE, getItemIconName, GUI_ITEM_ECONOMY_CODE
from gui.shared.gui_items.vehicle_equipment import VehicleEquipment
from gui.shared.gui_items.gui_item import HasStrCD
from gui.shared.gui_items.fitting_item import FittingItem, RentalInfoProvider
from gui.shared.gui_items.Tankman import Tankman
from gui.shared.money import MONEY_UNDEFINED, Currency, Money
from gui.shared.gui_items.gui_item_economics import ItemPrice, ItemPrices, ITEM_PRICE_EMPTY
from gui.shared.utils import makeSearchableString
from helpers import i18n, time_utils, dependency
from items import vehicles, tankmen, getTypeInfoByName, getTypeOfCompactDescr
from shared_utils import findFirst, CONST_CONTAINER
from skeletons.gui.game_control import IFalloutController, IIGRController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.server_events import IEventsCache

class VEHICLE_CLASS_NAME(CONST_CONTAINER):
    LIGHT_TANK = 'lightTank'
    MEDIUM_TANK = 'mediumTank'
    HEAVY_TANK = 'heavyTank'
    SPG = 'SPG'
    AT_SPG = 'AT-SPG'


VEHICLE_TYPES_ORDER = (VEHICLE_CLASS_NAME.LIGHT_TANK,
 VEHICLE_CLASS_NAME.MEDIUM_TANK,
 VEHICLE_CLASS_NAME.HEAVY_TANK,
 VEHICLE_CLASS_NAME.AT_SPG,
 VEHICLE_CLASS_NAME.SPG)
VEHICLE_TYPES_ORDER_INDICES = dict(((n, i) for i, n in enumerate(VEHICLE_TYPES_ORDER)))
UNKNOWN_VEHICLE_CLASS_ORDER = 100

def compareByVehTypeName(vehTypeA, vehTypeB):
    return VEHICLE_TYPES_ORDER_INDICES[vehTypeA] - VEHICLE_TYPES_ORDER_INDICES[vehTypeB]


def compareByVehTableTypeName(vehTypeA, vehTypeB):
    return VEHICLE_TABLE_TYPES_ORDER_INDICES[vehTypeA] - VEHICLE_TABLE_TYPES_ORDER_INDICES[vehTypeB]


VEHICLE_TABLE_TYPES_ORDER = (VEHICLE_CLASS_NAME.HEAVY_TANK,
 VEHICLE_CLASS_NAME.MEDIUM_TANK,
 VEHICLE_CLASS_NAME.LIGHT_TANK,
 VEHICLE_CLASS_NAME.AT_SPG,
 VEHICLE_CLASS_NAME.SPG)
VEHICLE_TABLE_TYPES_ORDER_INDICES = dict(((n, i) for i, n in enumerate(VEHICLE_TABLE_TYPES_ORDER)))
VEHICLE_TABLE_TYPES_ORDER_INDICES_REVERSED = dict(((n, i) for i, n in enumerate(reversed(VEHICLE_TABLE_TYPES_ORDER))))
VEHICLE_BATTLE_TYPES_ORDER = (VEHICLE_CLASS_NAME.HEAVY_TANK,
 VEHICLE_CLASS_NAME.MEDIUM_TANK,
 VEHICLE_CLASS_NAME.AT_SPG,
 VEHICLE_CLASS_NAME.LIGHT_TANK,
 VEHICLE_CLASS_NAME.SPG)
VEHICLE_BATTLE_TYPES_ORDER_INDICES = dict(((n, i) for i, n in enumerate(VEHICLE_BATTLE_TYPES_ORDER)))

class VEHICLE_TAGS(CONST_CONTAINER):
    PREMIUM = 'premium'
    PREMIUM_IGR = 'premiumIGR'
    CANNOT_BE_SOLD = 'cannot_be_sold'
    SECRET = 'secret'
    SPECIAL = 'special'
    OBSERVER = 'observer'
    DISABLED_IN_ROAMING = 'disabledInRoaming'
    EVENT = 'event_battles'
    EXCLUDED_FROM_SANDBOX = 'excluded_from_sandbox'
    TELECOM = 'telecom'
    FALLOUT = 'fallout'
    UNRECOVERABLE = 'unrecoverable'
    CREW_LOCKED = 'lockCrew'


class Vehicle(FittingItem, HasStrCD):
    __slots__ = ('__descriptor', '__customState', '_inventoryID', '_xp', '_dailyXPFactor', '_isElite', '_isFullyElite', '_clanLock', '_isUnique', '_rentPackages', '_hasRentPackages', '_isDisabledForBuy', '_isSelected', '_igrCustomizationsLayout', '_restorePrice', '_canTradeIn', '_canTradeOff', '_tradeOffPriceFactor', '_tradeOffPrice', '_searchableUserName', '_personalDiscountPrice', '_rotationGroupNum', '_rotationBattlesLeft', '_isRotationGroupLocked', '_isInfiniteRotationGroup', '_settings', '_lock', '_repairCost', '_health', '_gun', '_turret', '_engine', '_chassis', '_radio', '_fuelTank', '_optDevices', '_shells', '_equipment', '_equipmentLayout', '_bonuses', '_crewIndices', '_crew', '_lastCrew', '_hasModulesToSelect')
    NOT_FULL_AMMO_MULTIPLIER = 0.2
    MAX_RENT_MULTIPLIER = 2

    class VEHICLE_STATE:
        DAMAGED = 'damaged'
        EXPLODED = 'exploded'
        DESTROYED = 'destroyed'
        UNDAMAGED = 'undamaged'
        BATTLE = 'battle'
        IN_PREBATTLE = 'inPrebattle'
        LOCKED = 'locked'
        CREW_NOT_FULL = 'crewNotFull'
        AMMO_NOT_FULL = 'ammoNotFull'
        AMMO_NOT_FULL_EVENTS = 'ammoNotFullEvents'
        SERVER_RESTRICTION = 'serverRestriction'
        RENTAL_IS_OVER = 'rentalIsOver'
        IGR_RENTAL_IS_OVER = 'igrRentalIsOver'
        IN_PREMIUM_IGR_ONLY = 'inPremiumIgrOnly'
        GROUP_IS_NOT_READY = 'group_is_not_ready'
        NOT_PRESENT = 'notpresent'
        UNAVAILABLE = 'unavailable'
        FALLOUT_ONLY = 'fallout_only'
        FALLOUT_MIN = 'fallout_min'
        FALLOUT_MAX = 'fallout_max'
        FALLOUT_REQUIRED = 'fallout_required'
        FALLOUT_BROKEN = 'fallout_broken'
        UNSUITABLE_TO_QUEUE = 'unsuitableToQueue'
        UNSUITABLE_TO_UNIT = 'unsuitableToUnit'
        CUSTOM = (UNSUITABLE_TO_QUEUE, UNSUITABLE_TO_UNIT)
        DEAL_IS_OVER = 'dealIsOver'
        ROTATION_GROUP_UNLOCKED = 'rotationGroupUnlocked'
        ROTATION_GROUP_LOCKED = 'rotationGroupLocked'

    CAN_SELL_STATES = [VEHICLE_STATE.UNDAMAGED,
     VEHICLE_STATE.CREW_NOT_FULL,
     VEHICLE_STATE.AMMO_NOT_FULL,
     VEHICLE_STATE.GROUP_IS_NOT_READY,
     VEHICLE_STATE.FALLOUT_MIN,
     VEHICLE_STATE.FALLOUT_MAX,
     VEHICLE_STATE.FALLOUT_REQUIRED,
     VEHICLE_STATE.FALLOUT_BROKEN,
     VEHICLE_STATE.FALLOUT_ONLY,
     VEHICLE_STATE.UNSUITABLE_TO_QUEUE,
     VEHICLE_STATE.UNSUITABLE_TO_UNIT,
     VEHICLE_STATE.ROTATION_GROUP_UNLOCKED,
     VEHICLE_STATE.ROTATION_GROUP_LOCKED]
    GROUP_STATES = [VEHICLE_STATE.GROUP_IS_NOT_READY,
     VEHICLE_STATE.FALLOUT_MIN,
     VEHICLE_STATE.FALLOUT_MAX,
     VEHICLE_STATE.FALLOUT_REQUIRED,
     VEHICLE_STATE.FALLOUT_BROKEN]

    class VEHICLE_STATE_LEVEL:
        CRITICAL = 'critical'
        INFO = 'info'
        WARNING = 'warning'
        RENTED = 'rented'

    falloutCtrl = dependency.descriptor(IFalloutController)
    igrCtrl = dependency.descriptor(IIGRController)
    eventsCache = dependency.descriptor(IEventsCache)
    lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self, strCompactDescr = None, inventoryID = -1, typeCompDescr = None, proxy = None):
        if strCompactDescr is not None:
            vehDescr = vehicles.VehicleDescr(compactDescr=strCompactDescr)
        else:
            raise typeCompDescr is not None or AssertionError
            _, nID, innID = vehicles.parseIntCompactDescr(typeCompDescr)
            vehDescr = vehicles.VehicleDescr(typeID=(nID, innID))
        self.__descriptor = vehDescr
        HasStrCD.__init__(self, strCompactDescr)
        FittingItem.__init__(self, vehDescr.type.compactDescr, proxy)
        self._inventoryID = inventoryID
        self._xp = 0
        self._dailyXPFactor = -1
        self._isElite = False
        self._isFullyElite = False
        self._clanLock = 0
        self._isUnique = self.isHidden
        self._rentPackages = []
        self._hasRentPackages = False
        self._isDisabledForBuy = False
        self._isSelected = False
        self._igrCustomizationsLayout = {}
        self._restorePrice = None
        self._canTradeIn = False
        self._canTradeOff = False
        self._tradeOffPriceFactor = 0
        self._tradeOffPrice = MONEY_UNDEFINED
        if self.isPremiumIGR:
            self._searchableUserName = makeSearchableString(self.shortUserName)
        else:
            self._searchableUserName = makeSearchableString(self.userName)
        invData = dict()
        tradeInData = None
        if proxy is not None and proxy.inventory.isSynced() and proxy.stats.isSynced() and proxy.shop.isSynced() and proxy.vehicleRotation.isSynced() and proxy.recycleBin.isSynced():
            invDataTmp = proxy.inventory.getItems(GUI_ITEM_TYPE.VEHICLE, inventoryID)
            if invDataTmp is not None:
                invData = invDataTmp
            tradeInData = proxy.shop.tradeIn
            self._xp = proxy.stats.vehiclesXPs.get(self.intCD, self._xp)
            if proxy.shop.winXPFactorMode == WIN_XP_FACTOR_MODE.ALWAYS or self.intCD not in proxy.stats.multipliedVehicles and not self.isOnlyForEventBattles:
                self._dailyXPFactor = proxy.shop.dailyXPFactor
            self._isElite = len(vehDescr.type.unlocksDescrs) == 0 or self.intCD in proxy.stats.eliteVehicles
            self._isFullyElite = self.isElite and len([ data for data in vehDescr.type.unlocksDescrs if data[1] not in proxy.stats.unlocks ]) == 0
            clanDamageLock = proxy.stats.vehicleTypeLocks.get(self.intCD, {}).get(CLAN_LOCK, 0)
            clanNewbieLock = proxy.stats.globalVehicleLocks.get(CLAN_LOCK, 0)
            self._clanLock = clanDamageLock or clanNewbieLock
            self._isDisabledForBuy = self.intCD in proxy.shop.getNotToBuyVehicles()
            self._hasRentPackages = bool(proxy.shop.getVehicleRentPrices().get(self.intCD, {}))
            self._isSelected = bool(self.invID in proxy.stats.oldVehInvIDs)
            self._igrCustomizationsLayout = proxy.inventory.getIgrCustomizationsLayout().get(self._inventoryID, {})
            restoreConfig = proxy.shop.vehiclesRestoreConfig
            self._restorePrice = calcVehicleRestorePrice(self.buyPrices.itemPrice.defPrice, proxy.shop)
            self._restoreInfo = proxy.recycleBin.getVehicleRestoreInfo(self.intCD, restoreConfig.restoreDuration, restoreConfig.restoreCooldown)
            self._personalDiscountPrice = proxy.shop.getPersonalVehicleDiscountPrice(self.intCD)
            self._rotationGroupNum = proxy.vehicleRotation.getGroupNum(self.intCD)
            self._rotationBattlesLeft = proxy.vehicleRotation.getBattlesCount(self.rotationGroupNum)
            self._isRotationGroupLocked = proxy.vehicleRotation.isGroupLocked(self.rotationGroupNum)
            self._isInfiniteRotationGroup = proxy.vehicleRotation.isInfinite(self.rotationGroupNum)
        self._inventoryCount = 1 if len(invData.keys()) else 0
        data = invData.get('rent')
        if data is not None:
            self._rentInfo = RentalInfoProvider(isRented=True, *data)
        self._settings = invData.get('settings', 0)
        self._lock = invData.get('lock', (0, 0))
        self._repairCost, self._health = invData.get('repair', (0, 0))
        self._gun = self.itemsFactory.createVehicleGun(vehDescr.gun.compactDescr, proxy, vehDescr.gun)
        self._turret = self.itemsFactory.createVehicleTurret(vehDescr.turret.compactDescr, proxy, vehDescr.turret)
        self._engine = self.itemsFactory.createVehicleEngine(vehDescr.engine.compactDescr, proxy, vehDescr.engine)
        self._chassis = self.itemsFactory.createVehicleChassis(vehDescr.chassis.compactDescr, proxy, vehDescr.chassis)
        self._radio = self.itemsFactory.createVehicleRadio(vehDescr.radio.compactDescr, proxy, vehDescr.radio)
        self._fuelTank = self.itemsFactory.createVehicleFuelTank(vehDescr.fuelTank.compactDescr, proxy, vehDescr.fuelTank)
        sellPrice = self._calcSellPrice(proxy)
        defaultSellPrice = self._calcDefaultSellPrice(proxy)
        self._sellPrices = ItemPrices(itemPrice=ItemPrice(price=sellPrice, defPrice=defaultSellPrice), itemAltPrice=ITEM_PRICE_EMPTY)
        if tradeInData is not None and tradeInData.isEnabled and self.isPremium and not self.isPremiumIGR:
            self._tradeOffPriceFactor = tradeInData.sellPriceFactor
            tradeInLevels = tradeInData.allowedVehicleLevels
            self._canTradeIn = not self.isPurchased and not self.isHidden and self.isUnlocked and not self.isRestorePossible() and self.level in tradeInLevels
            self._canTradeOff = self.isPurchased and not self.canNotBeSold and self.intCD not in tradeInData.forbiddenVehicles and self.level in tradeInLevels
            if self.canTradeOff:
                self._tradeOffPrice = Money(gold=int(math.ceil(self.tradeOffPriceFactor * self.buyPrices.itemPrice.price.gold)))
        self._optDevices = self._parserOptDevs(vehDescr.optionalDevices, proxy)
        gunAmmoLayout = []
        for shell in self.gun.defaultAmmo:
            gunAmmoLayout += (shell.intCD, shell.defaultCount)

        self._shells = self._parseShells(invData.get('shells', list()), invData.get('shellsLayout', dict()).get(self.shellsLayoutIdx, gunAmmoLayout), proxy)
        self._equipment = VehicleEquipment(proxy, invData.get('eqs'))
        self._equipmentLayout = VehicleEquipment(proxy, invData.get('eqsLayout'))
        defaultCrew = [None] * len(vehDescr.type.crewRoles)
        crewList = invData.get('crew', defaultCrew)
        self._bonuses = self._calcCrewBonuses(crewList, proxy)
        self._crewIndices = dict([ (invID, idx) for idx, invID in enumerate(crewList) ])
        self._crew = self._buildCrew(crewList, proxy)
        self._lastCrew = invData.get('lastCrew')
        self._rentPackages = calcRentPackages(self, proxy)
        self._hasModulesToSelect = self.__hasModulesToSelect()
        self.__customState = ''
        return

    @property
    def buyPrices(self):
        """
        Get vehicle buy prices.
        If vehicle has personal discount and price with personal discount is less then its shop price with SSE actions
        then use personal discount price else shop price.
        """
        currency = self._buyPrices.itemPrice.price.getCurrency()
        if self._personalDiscountPrice is not None and self._personalDiscountPrice.get(currency) <= self._buyPrices.itemPrice.price.get(currency):
            currentPrice = self._personalDiscountPrice
        else:
            currentPrice = self._buyPrices.itemPrice.price
        if self.isRented and not self.rentalIsOver:
            buyPrice = currentPrice - self.rentCompensation
        else:
            buyPrice = currentPrice
        return ItemPrices(itemPrice=ItemPrice(price=buyPrice, defPrice=self._buyPrices.itemPrice.defPrice), itemAltPrice=self._buyPrices.itemAltPrice)

    @property
    def searchableUserName(self):
        return self._searchableUserName

    def getUnlockDescrByIntCD(self, intCD):
        for unlockIdx, data in enumerate(self.descriptor.type.unlocksDescrs):
            if intCD == data[1]:
                return (unlockIdx, data[0], set(data[2:]))

        return (-1, 0, set())

    def _calcSellPrice(self, proxy):
        if self.isRented:
            return MONEY_UNDEFINED
        price = self.sellPrices.itemPrice.price
        defaultDevices, installedDevices, _ = self.descriptor.getDevices()
        for defCompDescr, instCompDescr in izip(defaultDevices, installedDevices):
            if defCompDescr == instCompDescr:
                continue
            modulePrice = FittingItem(defCompDescr, proxy).sellPrices.itemPrice.price
            price = price - modulePrice
            modulePrice = FittingItem(instCompDescr, proxy).sellPrices.itemPrice.price
            price = price + modulePrice

        return price

    def _calcDefaultSellPrice(self, proxy):
        if self.isRented:
            return MONEY_UNDEFINED
        price = self.sellPrices.itemPrice.defPrice
        defaultDevices, installedDevices, _ = self.descriptor.getDevices()
        for defCompDescr, instCompDescr in izip(defaultDevices, installedDevices):
            if defCompDescr == instCompDescr:
                continue
            modulePrice = FittingItem(defCompDescr, proxy).sellPrices.itemPrice.defPrice
            price = price - modulePrice
            modulePrice = FittingItem(instCompDescr, proxy).sellPrices.itemPrice.defPrice
            price = price + modulePrice

        return price

    def _calcCrewBonuses(self, crew, proxy):
        bonuses = dict()
        bonuses['equipment'] = 0
        for eq in self.equipment.regularConsumables.getInstalledItems():
            bonuses['equipment'] += eq.crewLevelIncrease

        for battleBooster in self.equipment.battleBoosterConsumables.getInstalledItems():
            bonuses['equipment'] += battleBooster.getCrewBonus(self)

        bonuses['optDevices'] = self.descriptor.miscAttrs['crewLevelIncrease']
        bonuses['commander'] = 0
        commanderEffRoleLevel = 0
        bonuses['brotherhood'] = tankmen.getSkillsConfig().getSkill('brotherhood').crewLevelIncrease
        for tankmanID in crew:
            if tankmanID is None:
                bonuses['brotherhood'] = 0
                continue
            tmanInvData = proxy.inventory.getItems(GUI_ITEM_TYPE.TANKMAN, tankmanID)
            if not tmanInvData:
                continue
            tdescr = tankmen.TankmanDescr(compactDescr=tmanInvData['compDescr'])
            if 'brotherhood' not in tdescr.skills or tdescr.skills.index('brotherhood') == len(tdescr.skills) - 1 and tdescr.lastSkillLevel != tankmen.MAX_SKILL_LEVEL:
                bonuses['brotherhood'] = 0
            if tdescr.role == Tankman.ROLES.COMMANDER:
                factor, addition = tdescr.efficiencyOnVehicle(self.descriptor)
                commanderEffRoleLevel = round(tdescr.roleLevel * factor + addition)

        bonuses['commander'] += round((commanderEffRoleLevel + bonuses['brotherhood'] + bonuses['equipment']) / tankmen.COMMANDER_ADDITION_RATIO)
        return bonuses

    def _buildCrew(self, crew, proxy):
        crewItems = list()
        crewRoles = self.descriptor.type.crewRoles
        for idx, tankmanID in enumerate(crew):
            tankman = None
            if tankmanID is not None:
                tmanInvData = proxy.inventory.getItems(GUI_ITEM_TYPE.TANKMAN, tankmanID)
                tankman = self.itemsFactory.createTankman(strCompactDescr=tmanInvData['compDescr'], inventoryID=tankmanID, vehicle=self, proxy=proxy)
            crewItems.append((idx, tankman))

        return _sortCrew(crewItems, crewRoles)

    @staticmethod
    def __crewSort(t1, t2):
        if t1 is None or t2 is None:
            return 0
        else:
            return t1.__cmp__(t2)

    def _parseCompDescr(self, compactDescr):
        nId, innID = vehicles.parseVehicleCompactDescr(compactDescr)
        return (GUI_ITEM_TYPE.VEHICLE, nId, innID)

    def _parseShells(self, layoutList, defaultLayoutList, proxy):
        shellsDict = dict(((cd, count) for cd, count, _ in LayoutIterator(layoutList)))
        defaultsDict = dict(((cd, (count, isBoughtForCredits)) for cd, count, isBoughtForCredits in LayoutIterator(defaultLayoutList)))
        layoutList = list(layoutList)
        for shot in self.descriptor.gun.shots:
            cd = shot.shell.compactDescr
            if cd not in shellsDict:
                layoutList.extend([cd, 0])

        result = list()
        for intCD, count, _ in LayoutIterator(layoutList):
            defaultCount, isBoughtForCredits = defaultsDict.get(intCD, (0, False))
            result.append(self.itemsFactory.createShell(intCD, count, defaultCount, proxy, isBoughtForCredits))

        return result

    @classmethod
    def _parserOptDevs(cls, layoutList, proxy):
        result = list()
        for i in xrange(len(layoutList)):
            optDevDescr = layoutList[i]
            result.append(cls.itemsFactory.createOptionalDevice(optDevDescr.compactDescr, proxy) if optDevDescr is not None else None)

        return result

    @property
    def iconContour(self):
        return getContourIconPath(self.name)

    @property
    def iconUnique(self):
        return getUniqueIconPath(self.name, withLightning=False)

    @property
    def iconUniqueLight(self):
        return getUniqueIconPath(self.name, withLightning=True)

    @property
    def shellsLayoutIdx(self):
        return (self.turret.descriptor.compactDescr, self.gun.descriptor.compactDescr)

    @property
    def invID(self):
        return self._inventoryID

    @property
    def xp(self):
        return self._xp

    @property
    def dailyXPFactor(self):
        return self._dailyXPFactor

    @property
    def isElite(self):
        return self._isElite

    @property
    def isFullyElite(self):
        return self._isFullyElite

    @property
    def clanLock(self):
        return self._clanLock

    @property
    def isUnique(self):
        return self._isUnique

    @property
    def rentPackages(self):
        return self._rentPackages

    @property
    def hasRentPackages(self):
        return self._hasRentPackages

    @property
    def isDisabledForBuy(self):
        return self._isDisabledForBuy

    @property
    def isSelected(self):
        return self._isSelected

    @property
    def igrCustomizationsLayout(self):
        return self._igrCustomizationsLayout

    @property
    def restorePrice(self):
        return self._restorePrice

    @property
    def canTradeIn(self):
        return self._canTradeIn

    @property
    def canTradeOff(self):
        return self._canTradeOff

    @property
    def tradeOffPriceFactor(self):
        return self._tradeOffPriceFactor

    @property
    def tradeOffPrice(self):
        return self._tradeOffPrice

    @property
    def rotationGroupNum(self):
        return self._rotationGroupNum

    @property
    def rotationBattlesLeft(self):
        return self._rotationBattlesLeft

    @property
    def isRotationGroupLocked(self):
        return self._isRotationGroupLocked

    @property
    def isInfiniteRotationGroup(self):
        return self._isInfiniteRotationGroup

    @property
    def settings(self):
        return self._settings

    @property
    def lock(self):
        return self._lock

    @property
    def repairCost(self):
        return self._repairCost

    @property
    def health(self):
        return self._health

    @property
    def gun(self):
        return self._gun

    @gun.setter
    def gun(self, value):
        """
        This property can be set from cmp_view
        """
        self._gun = value

    @property
    def turret(self):
        return self._turret

    @turret.setter
    def turret(self, value):
        """
        This property can be set from cmp_view
        """
        self._turret = value

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, value):
        """
        This property can be set from cmp_view
        """
        self._engine = value

    @property
    def chassis(self):
        return self._chassis

    @chassis.setter
    def chassis(self, value):
        """
        This property can be set from cmp_view
        """
        self._chassis = value

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, value):
        """
        This property can be set from cmp_view
        """
        self._radio = value

    @property
    def fuelTank(self):
        return self._fuelTank

    @fuelTank.setter
    def fuelTank(self, value):
        """
        This property can be set from cmp_view
        """
        self._fuelTank = value

    @property
    def optDevices(self):
        return self._optDevices

    @property
    def shells(self):
        return self._shells

    @property
    def equipment(self):
        return self._equipment

    @property
    def equipmentLayout(self):
        return self._equipmentLayout

    @property
    def bonuses(self):
        return self._bonuses

    @property
    def crewIndices(self):
        return self._crewIndices

    @property
    def crew(self):
        return self._crew

    @crew.setter
    def crew(self, value):
        """
        Normally the property should not be changed outside, but params_helper.py does it.
        """
        self._crew = value

    @property
    def lastCrew(self):
        return self._lastCrew

    @property
    def hasModulesToSelect(self):
        return self._hasModulesToSelect

    @property
    def isRentable(self):
        return self.hasRentPackages and not self.isPurchased

    @property
    def isPurchased(self):
        return self.isInInventory and not self.rentInfo.isRented

    def isPreviewAllowed(self):
        return not self.isInInventory and not self.isSecret

    @property
    def rentExpiryTime(self):
        return self.rentInfo.rentExpiryTime

    @property
    def rentCompensation(self):
        return self.rentInfo.compensations

    @property
    def isRentAvailable(self):
        return self.maxRentDuration - self.rentLeftTime >= self.minRentDuration

    @property
    def minRentPrice(self):
        minRentPackage = self.getRentPackage()
        if minRentPackage is not None:
            return minRentPackage.get('rentPrice', MONEY_UNDEFINED)
        else:
            return MONEY_UNDEFINED

    @property
    def isRented(self):
        return self.rentInfo.isRented

    @property
    def rentLeftTime(self):
        return self.rentInfo.getTimeLeft()

    @property
    def maxRentDuration(self):
        if len(self.rentPackages) > 0:
            return max((item['days'] for item in self.rentPackages)) * self.MAX_RENT_MULTIPLIER * time_utils.ONE_DAY
        return 0

    @property
    def minRentDuration(self):
        if len(self.rentPackages) > 0:
            return min((item['days'] for item in self.rentPackages)) * time_utils.ONE_DAY
        return 0

    @property
    def rentalIsOver(self):
        return self.isRented and self.rentExpiryState and not self.isSelected

    @property
    def rentalIsActive(self):
        return self.isRented and not self.rentExpiryState

    @property
    def rentLeftBattles(self):
        return self.rentInfo.battlesLeft

    @property
    def rentExpiryState(self):
        return self.rentInfo.getExpiryState()

    @property
    def descriptor(self):
        return self.__descriptor

    @property
    def type(self):
        return set(vehicles.VEHICLE_CLASS_TAGS & self.tags).pop()

    @property
    def typeUserName(self):
        return getTypeUserName(self.type, self.isElite)

    @property
    def hasTurrets(self):
        vDescr = self.descriptor
        return len(vDescr.hull.fakeTurrets['lobby']) != len(vDescr.turrets)

    @property
    def hasBattleTurrets(self):
        vDescr = self.descriptor
        return len(vDescr.hull.fakeTurrets['battle']) != len(vDescr.turrets)

    @property
    def ammoMaxSize(self):
        return self.descriptor.gun.maxAmmo

    @property
    def isAmmoFull(self):
        return sum((s.count for s in self.shells)) >= self.ammoMaxSize * self.NOT_FULL_AMMO_MULTIPLIER

    @property
    def hasShells(self):
        return sum((s.count for s in self.shells)) > 0

    @property
    def hasCrew(self):
        return findFirst(lambda x: x[1] is not None, self.crew) is not None

    @property
    def hasEquipments(self):
        return findFirst(None, self.equipment.regularConsumables) is not None

    @property
    def hasOptionalDevices(self):
        return findFirst(None, self.optDevices) is not None

    @property
    def modelState(self):
        if self.health < 0:
            return Vehicle.VEHICLE_STATE.EXPLODED
        if self.repairCost > 0 and self.health == 0:
            return Vehicle.VEHICLE_STATE.DESTROYED
        return Vehicle.VEHICLE_STATE.UNDAMAGED

    def getState(self, isCurrnentPlayer = True):
        ms = self.modelState
        if not self.isInInventory and isCurrnentPlayer:
            ms = Vehicle.VEHICLE_STATE.NOT_PRESENT
        if self.isInBattle:
            ms = Vehicle.VEHICLE_STATE.BATTLE
        elif self.rentalIsOver:
            ms = Vehicle.VEHICLE_STATE.RENTAL_IS_OVER
            if self.isPremiumIGR:
                ms = Vehicle.VEHICLE_STATE.IGR_RENTAL_IS_OVER
            elif self.isTelecom:
                ms = Vehicle.VEHICLE_STATE.DEAL_IS_OVER
        elif self.isDisabledInPremIGR:
            ms = Vehicle.VEHICLE_STATE.IN_PREMIUM_IGR_ONLY
        elif self.isInPrebattle:
            ms = Vehicle.VEHICLE_STATE.IN_PREBATTLE
        elif self.isLocked:
            ms = Vehicle.VEHICLE_STATE.LOCKED
        elif self.isDisabledInRoaming:
            ms = Vehicle.VEHICLE_STATE.SERVER_RESTRICTION
        elif self.isRotationGroupLocked:
            ms = Vehicle.VEHICLE_STATE.ROTATION_GROUP_LOCKED
        ms = self.__checkUndamagedState(ms, isCurrnentPlayer)
        if ms in Vehicle.CAN_SELL_STATES and self.__customState:
            ms = self.__customState
        return (ms, self.__getStateLevel(ms))

    def setCustomState(self, state):
        raise state in Vehicle.VEHICLE_STATE.CUSTOM or AssertionError('State is not valid')
        self.__customState = state

    def getCustomState(self):
        return self.__customState

    def clearCustomState(self):
        self.__customState = ''

    def isCustomStateSet(self):
        return self.__customState != ''

    def __checkUndamagedState(self, state, isCurrnentPlayer = True):
        if state == Vehicle.VEHICLE_STATE.UNDAMAGED and isCurrnentPlayer:
            if self.isBroken:
                return Vehicle.VEHICLE_STATE.DAMAGED
            if not self.isCrewFull:
                return Vehicle.VEHICLE_STATE.CREW_NOT_FULL
            groupIsReady, groupState = self.isGroupReady()
            if self.isFalloutSelected and not groupIsReady:
                return groupState
            if not self.isAmmoFull:
                return Vehicle.VEHICLE_STATE.AMMO_NOT_FULL
            if self.isFalloutOnly() and not self.__isFalloutEnabled():
                return Vehicle.VEHICLE_STATE.FALLOUT_ONLY
            if not self.isRotationGroupLocked and self.rotationGroupNum != 0:
                return Vehicle.VEHICLE_STATE.ROTATION_GROUP_UNLOCKED
        return state

    @classmethod
    def __getEventVehicles(cls):
        return cls.eventsCache.getEventVehicles()

    def __getFalloutSelectedVehInvIDs(self):
        if self.__isFalloutEnabled():
            return self.falloutCtrl.getSelectedSlots()
        return ()

    def __getFalloutAvailableVehIDs(self):
        if self.__isFalloutEnabled():
            return self.falloutCtrl.getConfig().allowedVehicles
        return ()

    def __isFalloutEnabled(self):
        return self.falloutCtrl.isSelected()

    def isFalloutOnly(self):
        return _checkForTags(self.tags, VEHICLE_TAGS.FALLOUT)

    def isRotationApplied(self):
        return self.rotationGroupNum != 0

    def isGroupReady(self):
        if not self.falloutCtrl.isSelected():
            return (True, '')
        selectedVehicles = self.falloutCtrl.getSelectedVehicles()
        selectedVehiclesCount = len(selectedVehicles)
        config = self.falloutCtrl.getConfig()
        if self.falloutCtrl.mustSelectRequiredVehicle():
            return (False, Vehicle.VEHICLE_STATE.FALLOUT_REQUIRED)
        if selectedVehiclesCount < config.minVehiclesPerPlayer:
            return (False, Vehicle.VEHICLE_STATE.FALLOUT_MIN)
        if selectedVehiclesCount > config.maxVehiclesPerPlayer:
            return (False, Vehicle.VEHICLE_STATE.FALLOUT_MAX)
        for v in selectedVehicles:
            if v.isBroken or not v.isCrewFull or v.isInBattle or v.rentalIsOver or v.isDisabledInPremIGR:
                return (False, Vehicle.VEHICLE_STATE.FALLOUT_BROKEN)

        return (True, '')

    def __getStateLevel(self, state):
        if state in (Vehicle.VEHICLE_STATE.CREW_NOT_FULL,
         Vehicle.VEHICLE_STATE.DAMAGED,
         Vehicle.VEHICLE_STATE.EXPLODED,
         Vehicle.VEHICLE_STATE.DESTROYED,
         Vehicle.VEHICLE_STATE.SERVER_RESTRICTION,
         Vehicle.VEHICLE_STATE.RENTAL_IS_OVER,
         Vehicle.VEHICLE_STATE.IGR_RENTAL_IS_OVER,
         Vehicle.VEHICLE_STATE.AMMO_NOT_FULL_EVENTS,
         Vehicle.VEHICLE_STATE.UNSUITABLE_TO_QUEUE,
         Vehicle.VEHICLE_STATE.DEAL_IS_OVER,
         Vehicle.VEHICLE_STATE.UNSUITABLE_TO_UNIT,
         Vehicle.VEHICLE_STATE.ROTATION_GROUP_LOCKED):
            return Vehicle.VEHICLE_STATE_LEVEL.CRITICAL
        if state in (Vehicle.VEHICLE_STATE.UNDAMAGED, Vehicle.VEHICLE_STATE.ROTATION_GROUP_UNLOCKED):
            return Vehicle.VEHICLE_STATE_LEVEL.INFO
        return Vehicle.VEHICLE_STATE_LEVEL.WARNING

    @property
    def isPremium(self):
        return _checkForTags(self.tags, VEHICLE_TAGS.PREMIUM)

    @property
    def isPremiumIGR(self):
        return _checkForTags(self.tags, VEHICLE_TAGS.PREMIUM_IGR)

    @property
    def isSecret(self):
        return _checkForTags(self.tags, VEHICLE_TAGS.SECRET)

    @property
    def isSpecial(self):
        return _checkForTags(self.tags, VEHICLE_TAGS.SPECIAL)

    @property
    def isExcludedFromSandbox(self):
        return _checkForTags(self.tags, VEHICLE_TAGS.EXCLUDED_FROM_SANDBOX)

    @property
    def isObserver(self):
        return _checkForTags(self.tags, VEHICLE_TAGS.OBSERVER)

    @property
    def isEvent(self):
        return self.isOnlyForEventBattles and self in Vehicle.__getEventVehicles()

    @property
    def isFalloutSelected(self):
        return self.invID in self.__getFalloutSelectedVehInvIDs()

    @property
    def isFalloutAvailable(self):
        return not self.isOnlyForEventBattles and self.intCD in self.__getFalloutAvailableVehIDs()

    @property
    def isDisabledInRoaming(self):
        return _checkForTags(self.tags, VEHICLE_TAGS.DISABLED_IN_ROAMING) and self.lobbyContext.getServerSettings().roaming.isInRoaming()

    @property
    def canNotBeSold(self):
        return _checkForTags(self.tags, VEHICLE_TAGS.CANNOT_BE_SOLD)

    @property
    def isUnrecoverable(self):
        return _checkForTags(self.tags, VEHICLE_TAGS.UNRECOVERABLE)

    @property
    def isCrewLocked(self):
        return _checkForTags(self.tags, VEHICLE_TAGS.CREW_LOCKED)

    @property
    def isDisabledInPremIGR(self):
        return self.isPremiumIGR and self.igrCtrl.getRoomType() != constants.IGR_TYPE.PREMIUM

    @property
    def name(self):
        return self.descriptor.type.name

    @property
    def userName(self):
        return getUserName(self.descriptor.type)

    @property
    def longUserName(self):
        typeInfo = getTypeInfoByName('vehicle')
        tagsDump = [ typeInfo['tags'][tag]['userString'] for tag in self.tags if typeInfo['tags'][tag]['userString'] != '' ]
        return '%s %s' % (''.join(tagsDump), getUserName(self.descriptor.type))

    @property
    def shortUserName(self):
        return getShortUserName(self.descriptor.type)

    @property
    def level(self):
        return self.descriptor.type.level

    @property
    def fullDescription(self):
        if self.descriptor.type.description.find('_descr') == -1:
            return self.descriptor.type.description
        return ''

    @property
    def tags(self):
        return self.descriptor.type.tags

    @property
    def rotationGroupIdx(self):
        return self.rotationGroupNum - 1

    @property
    def canSell(self):
        if not self.isInInventory:
            return False
        st, _ = self.getState()
        if self.isRented:
            if not self.rentalIsOver:
                return False
            if st in (self.VEHICLE_STATE.RENTAL_IS_OVER, self.VEHICLE_STATE.IGR_RENTAL_IS_OVER):
                st = self.__checkUndamagedState(self.modelState)
        return st in self.CAN_SELL_STATES and not _checkForTags(self.tags, VEHICLE_TAGS.CANNOT_BE_SOLD)

    @property
    def isLocked(self):
        return self.lock[0] != LOCK_REASON.NONE

    @property
    def isInBattle(self):
        return self.lock[0] == LOCK_REASON.ON_ARENA

    @property
    def isInPrebattle(self):
        return self.lock[0] in (LOCK_REASON.PREBATTLE, LOCK_REASON.UNIT)

    @property
    def isAwaitingBattle(self):
        return self.lock[0] == LOCK_REASON.IN_QUEUE

    @property
    def isInUnit(self):
        return self.lock[0] == LOCK_REASON.UNIT

    @property
    def typeOfLockingArena(self):
        if not self.isLocked:
            return None
        else:
            return self.lock[1]
            return None

    @property
    def isBroken(self):
        return self.repairCost > 0

    @property
    def isAlive(self):
        return not self.isBroken and not self.isLocked

    @property
    def isCrewFull(self):
        crew = map(lambda (role, tman): tman, self.crew)
        return None not in crew and len(crew)

    @property
    def isOnlyForEventBattles(self):
        return _checkForTags(self.tags, VEHICLE_TAGS.EVENT)

    @property
    def isTelecom(self):
        return _checkForTags(self.tags, VEHICLE_TAGS.TELECOM)

    @property
    def isTelecomDealOver(self):
        return self.isTelecom and self.rentExpiryState

    def hasLockMode(self):
        isBS = prb_getters.isBattleSession()
        if isBS:
            isBSVehicleLockMode = bool(prb_getters.getPrebattleSettings()[PREBATTLE_SETTING_NAME.VEHICLE_LOCK_MODE])
            if isBSVehicleLockMode and self.clanLock > 0:
                return True
        return False

    def isReadyToPrebattle(self, checkForRent = True):
        if checkForRent and self.rentalIsOver:
            return False
        if self.isFalloutOnly() and not self.__isFalloutEnabled():
            return False
        if not self.isGroupReady()[0]:
            return False
        result = not self.hasLockMode()
        if result:
            result = not self.isBroken and self.isCrewFull and not self.isDisabledInPremIGR and not self.isInBattle and not self.isRotationGroupLocked
        return result

    @property
    def isReadyToFight(self):
        if self.__isFalloutEnabled() and not self.isFalloutSelected:
            return True
        if self.rentalIsOver:
            return False
        if self.isFalloutOnly() and not self.__isFalloutEnabled():
            return False
        if not self.isGroupReady()[0]:
            return False
        result = not self.hasLockMode()
        if result:
            result = self.isAlive and self.isCrewFull and not self.isDisabledInRoaming and not self.isDisabledInPremIGR and not self.isRotationGroupLocked
        return result

    @property
    def isXPToTman(self):
        return bool(self.settings & VEHICLE_SETTINGS_FLAG.XP_TO_TMAN)

    @property
    def isAutoRepair(self):
        return bool(self.settings & VEHICLE_SETTINGS_FLAG.AUTO_REPAIR)

    @property
    def isAutoLoad(self):
        return bool(self.settings & VEHICLE_SETTINGS_FLAG.AUTO_LOAD)

    @property
    def isAutoEquip(self):
        return bool(self.settings & VEHICLE_SETTINGS_FLAG.AUTO_EQUIP)

    def isAutoBattleBoosterEquip(self):
        return bool(self.settings & VEHICLE_SETTINGS_FLAG.AUTO_EQUIP_BOOSTER)

    @property
    def isFavorite(self):
        return bool(self.settings & VEHICLE_SETTINGS_FLAG.GROUP_0)

    def isAutoLoadFull(self):
        if self.isAutoLoad:
            for shell in self.shells:
                if shell.count != shell.defaultCount:
                    return False

        return True

    def isAutoEquipFull(self):
        if self.isAutoEquip:
            return self.equipment.regularConsumables == self.equipmentLayout.regularConsumables
        else:
            return True

    def mayPurchase(self, money):
        if self.isOnlyForEventBattles:
            return (False, 'isDisabledForBuy')
        if self.isDisabledForBuy:
            return (False, 'isDisabledForBuy')
        if self.isPremiumIGR:
            return (False, 'premiumIGR')
        return super(Vehicle, self).mayPurchase(money)

    def mayRent(self, money):
        if getattr(BigWorld.player(), 'isLongDisconnectedFromCenter', False):
            return (False, GUI_ITEM_ECONOMY_CODE.CENTER_UNAVAILABLE)
        elif self.isDisabledForBuy and not self.isRentable:
            return (False, GUI_ITEM_ECONOMY_CODE.RENTAL_DISABLED)
        elif self.isRentable and not self.isRentAvailable:
            return (False, GUI_ITEM_ECONOMY_CODE.RENTAL_TIME_EXCEEDED)
        minRentPrice = self.minRentPrice
        if minRentPrice:
            return self._isEnoughMoney(minRentPrice, money)
        else:
            return (False, GUI_ITEM_ECONOMY_CODE.NO_RENT_PRICE)

    def mayRestore(self, money):
        """
        Check if vehicle may restore for money
        :param money:<Money>
        :return: tuple(mayRestore:<bool>, errorReason:<str>
        """
        if getattr(BigWorld.player(), 'isLongDisconnectedFromCenter', False):
            return (False, GUI_ITEM_ECONOMY_CODE.CENTER_UNAVAILABLE)
        if not self.isRestoreAvailable() or constants.IS_CHINA and self.rentalIsActive:
            return (False, GUI_ITEM_ECONOMY_CODE.RESTORE_DISABLED)
        return self._isEnoughMoney(self.restorePrice, money)

    def mayRestoreWithExchange(self, money, exchangeRate):
        """
        Check if vehicle may restore with money exchange
        :param money:<Money>
        :param exchangeRate: <int> gold for credits exchange rate
        :return:
        """
        mayRestore, reason = self.mayRestore(money)
        if mayRestore:
            return mayRestore
        elif reason == GUI_ITEM_ECONOMY_CODE.NOT_ENOUGH_CREDITS and money.isSet(Currency.GOLD):
            money = money.exchange(Currency.GOLD, Currency.CREDITS, exchangeRate, default=0)
            mayRestore, reason = self._isEnoughMoney(self.restorePrice, money)
            return mayRestore
        else:
            return False

    def getRentPackage(self, days = None):
        """
        Returns rentPackage with min rent price if days is None, else return rentPackage
        for selected daysPacket
        :param days: dict ('days' : <int-type>, 'rentPrice' : <int-type>,
                           'defaultRentPrice' : <int-type>)
        :return: Rent package or None
        """
        if days is not None:
            for package in self.rentPackages:
                if package.get('days', None) == days:
                    return package

        elif len(self.rentPackages) > 0:
            return min(self.rentPackages, key=itemgetter('rentPrice'))
        return

    def getGUIEmblemID(self):
        return self.icon

    def getRentPackageActionPrc(self, days = None):
        package = self.getRentPackage(days)
        if package:
            return getActionPrc(package['rentPrice'], package['defaultRentPrice'])
        return 0

    def getAutoUnlockedItems(self):
        return self.descriptor.type.autounlockedItems[:]

    def getAutoUnlockedItemsMap(self):
        return dict(map(lambda nodeCD: (vehicles.getItemByCompactDescr(nodeCD).itemTypeName, nodeCD), self.descriptor.type.autounlockedItems))

    def getUnlocksDescrs(self):
        for unlockIdx, data in enumerate(self.descriptor.type.unlocksDescrs):
            yield (unlockIdx,
             data[0],
             data[1],
             set(data[2:]))

    def getUnlocksDescr(self, unlockIdx):
        try:
            data = self.descriptor.type.unlocksDescrs[unlockIdx]
        except IndexError:
            data = (0, 0, set())

        return (data[0], data[1], set(data[2:]))

    def getPerfectCrew(self):
        return self.getCrewBySkillLevels(100)

    def getCrewWithoutSkill(self, skillName):
        """
        Gets crew without selected skill
        if selected skill is last in tankman skills and its level less than MAX_SKILL_LEVEL,
        then remove this skill and change tankman lastSkillLevel
        """
        crewItems = list()
        crewRoles = self.descriptor.type.crewRoles
        for slotIdx, tman in self.crew:
            if tman and skillName in tman.skillsMap:
                tmanDescr = tman.descriptor
                skills = tmanDescr.skills[:]
                if tmanDescr.skillLevel(skillName) < tankmen.MAX_SKILL_LEVEL:
                    lastSkillLevel = tankmen.MAX_SKILL_LEVEL
                else:
                    lastSkillLevel = tmanDescr.lastSkillLevel
                skills.remove(skillName)
                unskilledTman = self.itemsFactory.createTankman(tankmen.generateCompactDescr(tmanDescr.getPassport(), tmanDescr.vehicleTypeID, tmanDescr.role, tmanDescr.roleLevel, skills, lastSkillLevel), vehicle=self)
                crewItems.append((slotIdx, unskilledTman))
            else:
                crewItems.append((slotIdx, tman))

        return _sortCrew(crewItems, crewRoles)

    def getCrewBySkillLevels(self, defRoleLevel, skillsByIdxs = None, levelByIdxs = None, nativeVehsByIdxs = None):
        """
        Generate sorted list of tankmans with provided skills levels and provided skills
        :param defRoleLevel: desired skills levels
        :param skillsByIdxs: desired skills for particular members (index of member) or crew,
        dict-{tankmanIndex: [skill, skill, ...], ...}
        :param levelByIdxs: desired roleLevel for particular members (index of member) or crew,
        dict-{tankmanIndex: roleLevel, ...}
        :param nativeVehsByIdxs: desired native vehicles references for particular members (index of member) or crew,
        dict-{tankmanIndex: nativeVehicleReference, ...}
        :return: list of tuples [(role, gui_items.Tankman), (role, gui_items.Tankman), ...] sorted by tankmans roles
        """
        skillsByIdxs = skillsByIdxs or {}
        levelByIdxs = levelByIdxs or {}
        nativeVehsByIdxs = nativeVehsByIdxs or {}
        crewItems = list()
        crewRoles = self.descriptor.type.crewRoles
        for idx, _ in enumerate(crewRoles):
            defRoleLevel = levelByIdxs.get(idx, defRoleLevel)
            if defRoleLevel is not None:
                role = self.descriptor.type.crewRoles[idx][0]
                nativeVehicle = nativeVehsByIdxs.get(idx)
                if nativeVehicle is not None:
                    nationID, vehicleTypeID = nativeVehicle.descriptor.type.id
                else:
                    nationID, vehicleTypeID = self.descriptor.type.id
                tankman = self.itemsFactory.createTankman(tankmen.generateCompactDescr(tankmen.generatePassport(nationID), vehicleTypeID, role, defRoleLevel, skillsByIdxs.get(idx, [])), vehicle=self)
            else:
                tankman = None
            crewItems.append((idx, tankman))

        return _sortCrew(crewItems, crewRoles)

    def getCustomizedDescriptor(self):
        if self.invID > 0:
            igrRoomType = self.igrCtrl.getRoomType()
            igrLayout = {self.invID: self.igrCustomizationsLayout}
            updatedVehCompactDescr = getCustomizedVehCompDescr(igrLayout, self.invID, igrRoomType, self.descriptor.makeCompactDescr())
            serverSettings = self.lobbyContext.getServerSettings()
            if serverSettings is not None and serverSettings.roaming.isInRoaming():
                updatedVehCompactDescr = vehicles.stripCustomizationFromVehicleCompactDescr(updatedVehCompactDescr, True, True, False)[0]
            newDescriptor = vehicles.VehicleDescr(compactDescr=updatedVehCompactDescr)
            newDescriptor.activeGunShotIndex = self.descriptor.activeGunShotIndex
            return newDescriptor
        else:
            return self.descriptor
            return

    def isRestorePossible(self):
        """
        Check the possibility of vehicle restore, right now or in future
        :return: <bool>
        """
        if not self.isPurchased and not self.isUnrecoverable and self.lobbyContext.getServerSettings().isVehicleRestoreEnabled() and self.restoreInfo is not None:
            return self.restoreInfo.isRestorePossible()
        else:
            return False

    def isRestoreAvailable(self):
        """
        Check if vehicle restore is available right now
        restore can be limited or unlimitid in time
        :return: <bool>
        """
        return self.isRestorePossible() and not self.restoreInfo.isInCooldown()

    def hasLimitedRestore(self):
        """
        Check if vehicle has limited in time restore and restore left time is not finished
        :return: <bool>
        """
        return self.isRestorePossible() and self.restoreInfo.isLimited() and self.restoreInfo.getRestoreTimeLeft() > 0

    def hasRestoreCooldown(self):
        """
        Check if vehicle restore is in cooldown
        :return: <bool>
        """
        return self.isRestorePossible() and self.restoreInfo.isInCooldown()

    def isRecentlyRestored(self):
        """
        Check if vehicle was already restored and restore cooldown is not finished
        :return: <bool>
        """
        if self.restoreInfo is not None:
            return self.isPurchased and self.restoreInfo.isInCooldown()
        else:
            return False

    def __cmp__(self, other):
        if self.isRestorePossible() and not other.isRestorePossible():
            return -1
        if not self.isRestorePossible() and other.isRestorePossible():
            return 1
        if self.isRestorePossible() and other.isRestorePossible():
            return cmp(other.hasLimitedRestore(), self.hasLimitedRestore()) or cmp(self.restoreInfo.getRestoreTimeLeft(), other.restoreInfo.getRestoreTimeLeft())
        return super(Vehicle, self).__cmp__(other)

    def __eq__(self, other):
        if other is None:
            return False
        else:
            return self.descriptor.type.id == other.descriptor.type.id

    def __repr__(self):
        return 'Vehicle<id:%d, intCD:%d, nation:%d, lock:%s>' % (self.invID,
         self.intCD,
         self.nationID,
         self.lock)

    def _getShortInfo(self, vehicle = None, expanded = False):
        description = i18n.makeString('#menu:descriptions/' + self.itemTypeName)
        caliber = self.descriptor.gun.shots[0].shell.caliber
        armor = findVehicleArmorMinMax(self.descriptor)
        return description % {'weight': BigWorld.wg_getNiceNumberFormat(float(self.descriptor.physics['weight']) / 1000),
         'hullArmor': BigWorld.wg_getIntegralFormat(armor[1]),
         'caliber': BigWorld.wg_getIntegralFormat(caliber)}

    def _sortByType(self, other):
        return compareByVehTypeName(self.type, other.type)

    def __hasModulesToSelect(self):
        components = []
        for moduleCD in self.descriptor.type.installableComponents:
            moduleType = getTypeOfCompactDescr(moduleCD)
            if moduleType == GUI_ITEM_TYPE.FUEL_TANK:
                continue
            if moduleType in components:
                return True
            components.append(moduleType)

        return False


def getTypeUserName(vehType, isElite):
    if isElite:
        return i18n.makeString('#menu:header/vehicleType/elite/%s' % vehType)
    else:
        return i18n.makeString('#menu:header/vehicleType/%s' % vehType)


def getTypeShortUserName(vehType):
    return i18n.makeString('#menu:classes/short/%s' % vehType)


def _getLevelIconName(vehLevel, postfix = ''):
    return 'tank_level_%s%d.png' % (postfix, int(vehLevel))


def getLevelBigIconPath(vehLevel):
    return '../maps/icons/levels/%s' % _getLevelIconName(vehLevel, 'big_')


def getLevelSmallIconPath(vehLevel):
    return '../maps/icons/levels/%s' % _getLevelIconName(vehLevel, 'small_')


def getLevelIconPath(vehLevel):
    return '../maps/icons/levels/%s' % _getLevelIconName(vehLevel)


def getIconPath(vehicleName):
    return '../maps/icons/vehicle/%s' % getItemIconName(vehicleName)


def getContourIconPath(vehicleName):
    return '../maps/icons/vehicle/contour/%s' % getItemIconName(vehicleName)


def getSmallIconPath(vehicleName):
    return '../maps/icons/vehicle/small/%s' % getItemIconName(vehicleName)


def getUniqueIconPath(vehicleName, withLightning = False):
    if withLightning:
        return '../maps/icons/vehicle/unique/%s' % getItemIconName(vehicleName)
    else:
        return '../maps/icons/vehicle/unique/normal_%s' % getItemIconName(vehicleName)


def getTypeIconName(vehicleType):
    return '%s.png' % vehicleType


def getTypeEliteIconName(vehicleType, isElite):
    if isElite:
        return '%s_elite.png' % vehicleType
    else:
        return getTypeIconName(vehicleType)


def getTypeSmallIconPath(vehicleType):
    return '../maps/icons/vehicleTypes/%s' % getTypeIconName(vehicleType)


def getTypeBigIconPath(vehicleType, isElite):
    return '../maps/icons/vehicleTypes/big/%s' % getTypeEliteIconName(vehicleType, isElite)


def getUserName(vehicleType, textPrefix = False):
    return _getActualName(vehicleType.userString, vehicleType.tags, textPrefix)


def getShortUserName(vehicleType, textPrefix = False):
    return _getActualName(vehicleType.shortUserString, vehicleType.tags, textPrefix)


def _getActualName(name, tags, textPrefix = False):
    if _checkForTags(tags, VEHICLE_TAGS.PREMIUM_IGR):
        if textPrefix:
            return i18n.makeString(ITEM_TYPES.MARKER_IGR, vehName=name)
        return makeHtmlString('html_templates:igr/premium-vehicle', 'name', {'vehicle': name})
    return name


def _checkForTags(vTags, tags):
    if not hasattr(tags, '__iter__'):
        tags = (tags,)
    return bool(vTags & frozenset(tags))


def findVehicleArmorMinMax(vd):

    def findComponentArmorMinMax(armor, minMax):
        for value in armor:
            if value != 0:
                if minMax is None:
                    minMax = [value, value]
                else:
                    minMax[0] = min(minMax[0], value)
                    minMax[1] = max(minMax[1], value)

        return minMax

    minMax = None
    minMax = findComponentArmorMinMax(vd.hull.primaryArmor, minMax)
    for turrets in vd.type.turrets:
        for turret in turrets:
            minMax = findComponentArmorMinMax(turret.primaryArmor, minMax)

    return minMax


def _sortCrew(crewItems, crewRoles):
    RO = Tankman.TANKMEN_ROLES_ORDER
    return sorted(crewItems, cmp=lambda a, b: RO[crewRoles[a[0]][0]] - RO[crewRoles[b[0]][0]])


def getLobbyDescription(vehicle):
    return text_styles.stats(i18n.makeString('#menu:header/level/%s' % vehicle.level)) + ' ' + text_styles.main(i18n.makeString('#menu:header/level', vTypeName=getTypeUserName(vehicle.type, vehicle.isElite)))


def getOrderByVehicleClass(className = None):
    if className and className in VEHICLE_BATTLE_TYPES_ORDER_INDICES:
        result = VEHICLE_BATTLE_TYPES_ORDER_INDICES[className]
    else:
        result = UNKNOWN_VEHICLE_CLASS_ORDER
    return result


def getVehicleClassTag(tags):
    subSet = vehicles.VEHICLE_CLASS_TAGS & tags
    result = None
    if len(subSet):
        result = list(subSet).pop()
    return result


_VEHICLE_STATE_TO_ICON = {Vehicle.VEHICLE_STATE.BATTLE: RES_ICONS.MAPS_ICONS_VEHICLESTATES_BATTLE,
 Vehicle.VEHICLE_STATE.IN_PREBATTLE: RES_ICONS.MAPS_ICONS_VEHICLESTATES_INPREBATTLE,
 Vehicle.VEHICLE_STATE.DAMAGED: RES_ICONS.MAPS_ICONS_VEHICLESTATES_DAMAGED,
 Vehicle.VEHICLE_STATE.DESTROYED: RES_ICONS.MAPS_ICONS_VEHICLESTATES_DAMAGED,
 Vehicle.VEHICLE_STATE.EXPLODED: RES_ICONS.MAPS_ICONS_VEHICLESTATES_DAMAGED,
 Vehicle.VEHICLE_STATE.CREW_NOT_FULL: RES_ICONS.MAPS_ICONS_VEHICLESTATES_CREWNOTFULL,
 Vehicle.VEHICLE_STATE.RENTAL_IS_OVER: RES_ICONS.MAPS_ICONS_VEHICLESTATES_RENTALISOVER,
 Vehicle.VEHICLE_STATE.UNSUITABLE_TO_UNIT: RES_ICONS.MAPS_ICONS_VEHICLESTATES_UNSUITABLETOUNIT,
 Vehicle.VEHICLE_STATE.UNSUITABLE_TO_QUEUE: RES_ICONS.MAPS_ICONS_VEHICLESTATES_UNSUITABLETOUNIT,
 Vehicle.VEHICLE_STATE.GROUP_IS_NOT_READY: RES_ICONS.MAPS_ICONS_VEHICLESTATES_GROUP_IS_NOT_READY}

def getVehicleStateIcon(vState):
    """
    Gets status icon by vehicle state
    :param vState: one of Vehicle.VEHICLE_STATE
    :return: string(empty string means there is no icon for the state)
    """
    if vState in _VEHICLE_STATE_TO_ICON:
        icon = _VEHICLE_STATE_TO_ICON[vState]
    else:
        icon = ''
    return icon


def getBattlesLeft(vehicle):
    if vehicle.isInfiniteRotationGroup:
        return i18n.makeString('#menu:infinitySymbol')
    else:
        return str(vehicle.rotationBattlesLeft)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\Vehicle.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:49:38 St�edn� Evropa (letn� �as)
