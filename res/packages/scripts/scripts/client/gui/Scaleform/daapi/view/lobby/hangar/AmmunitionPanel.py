# 2017.08.29 21:46:58 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/AmmunitionPanel.py
from items.vehicles import NUM_OPTIONAL_DEVICE_SLOTS
from CurrentVehicle import g_currentVehicle
from gui import makeHtmlString
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.shared.fitting_slot_vo import FittingSlotVO, HangarFittingSlotVO
from gui.Scaleform.daapi.view.meta.AmmunitionPanelMeta import AmmunitionPanelMeta
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.ITEM_TYPES import ITEM_TYPES
from gui.shared import event_dispatcher as shared_events
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.shared.events import LoadViewEvent
from gui.shared.gui_items import GUI_ITEM_TYPE_INDICES, GUI_ITEM_TYPE, GUI_ITEM_TYPE_NAMES
from gui.shared.gui_items.Vehicle import Vehicle
from gui.shared.gui_items.vehicle_equipment import BATTLE_BOOSTER_LAYOUT_SIZE
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import i18n, dependency
from skeletons.gui.game_control import IFalloutController
from skeletons.gui.shared import IItemsCache
ARTEFACTS_SLOTS = (GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.OPTIONALDEVICE], GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.EQUIPMENT])
_BOOSTERS_SLOTS = (GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.BATTLE_BOOSTER],)
FITTING_MODULES = (GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.CHASSIS],
 GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.TURRET],
 GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.GUN],
 GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.ENGINE],
 GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.RADIO])
FITTING_SLOTS = FITTING_MODULES + ARTEFACTS_SLOTS
HANGAR_FITTING_SLOTS = FITTING_SLOTS + _BOOSTERS_SLOTS

@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def getFittingSlotsData(vehicle, slotsRange, VoClass = None, itemsCache = None):
    devices = []
    VoClass = VoClass or FittingSlotVO
    for slotType in slotsRange:
        data = itemsCache.items.getItems(GUI_ITEM_TYPE_INDICES[slotType], REQ_CRITERIA.CUSTOM(lambda item: item.isInstalled(vehicle))).values()
        if slotType in ARTEFACTS_SLOTS:
            for slotId in xrange(NUM_OPTIONAL_DEVICE_SLOTS):
                devices.append(VoClass(data, vehicle, slotType, slotId, TOOLTIPS_CONSTANTS.HANGAR_MODULE))

        elif slotType in _BOOSTERS_SLOTS:
            for slotId in xrange(BATTLE_BOOSTER_LAYOUT_SIZE):
                devices.append(VoClass(data, vehicle, slotType, slotId, tooltipType=TOOLTIPS_CONSTANTS.BATTLE_BOOSTER))

        else:
            devices.append(VoClass(data, vehicle, slotType, tooltipType=TOOLTIPS_CONSTANTS.HANGAR_MODULE))

    return devices


def getAmmo(shells):
    outcome = []
    for shell in shells:
        if shell.isHidden:
            continue
        outcome.append({'id': str(shell.intCD),
         'type': shell.type,
         'label': ITEM_TYPES.shell_kindsabbreviation(shell.type),
         'icon': '../maps/icons/ammopanel/ammo/%s' % shell.descriptor.icon[0],
         'count': shell.count,
         'tooltip': '',
         'tooltipType': TOOLTIPS_CONSTANTS.HANGAR_SHELL})

    return outcome


class AmmunitionPanel(AmmunitionPanelMeta):
    itemsCache = dependency.descriptor(IItemsCache)
    falloutCtrl = dependency.descriptor(IFalloutController)

    def update(self):
        self._update()

    def showTechnicalMaintenance(self):
        self.fireEvent(LoadViewEvent(VIEW_ALIAS.TECHNICAL_MAINTENANCE), EVENT_BUS_SCOPE.LOBBY)

    def showCustomization(self):
        self.fireEvent(LoadViewEvent(VIEW_ALIAS.LOBBY_CUSTOMIZATION), EVENT_BUS_SCOPE.LOBBY)

    def toRentContinue(self):
        if g_currentVehicle.isPresent():
            vehicle = g_currentVehicle.item
            canBuyOrRent, _ = vehicle.mayObtainForMoney(self.itemsCache.items.stats.money)
            if vehicle.isRentable and vehicle.rentalIsOver and canBuyOrRent:
                shared_events.showVehicleBuyDialog(vehicle)

    def showModuleInfo(self, itemCD):
        if itemCD is not None and int(itemCD) > 0:
            shared_events.showModuleInfo(itemCD, g_currentVehicle.item.descriptor)
        return

    def _populate(self):
        super(AmmunitionPanel, self)._populate()
        g_clientUpdateManager.addCallbacks({'inventory': self.__inventoryUpdateCallBack})
        self.falloutCtrl.onSettingsChanged += self._updateFalloutSettings
        self.update()

    def _dispose(self):
        self.falloutCtrl.onSettingsChanged -= self._updateFalloutSettings
        g_clientUpdateManager.removeObjectCallbacks(self)
        super(AmmunitionPanel, self)._dispose()

    def _updateFalloutSettings(self):
        self._update()

    def _update(self):
        if g_currentVehicle.isPresent():
            vehicle = g_currentVehicle.item
            statusId, msg, msgLvl = g_currentVehicle.getHangarMessage()
            rentAvailable = False
            if statusId == Vehicle.VEHICLE_STATE.RENTAL_IS_OVER:
                canBuyOrRent, _ = vehicle.mayObtainForMoney(self.itemsCache.items.stats.money)
                rentAvailable = vehicle.isRentable and canBuyOrRent
            isBackground = statusId == Vehicle.VEHICLE_STATE.NOT_PRESENT
            msgString = makeHtmlString('html_templates:vehicleStatus', msgLvl, {'message': i18n.makeString(msg)})
            self.__updateDevices(vehicle)
            self.as_updateVehicleStatusS({'message': msgString,
             'rentAvailable': rentAvailable,
             'isBackground': isBackground})

    def __inventoryUpdateCallBack(self, *args):
        self.update()

    def __updateDevices(self, vehicle):
        shells = []
        stateWarning = False
        if g_currentVehicle.isPresent():
            stateWarning = vehicle.isBroken or not vehicle.isAmmoFull or not g_currentVehicle.isAutoLoadFull() or not g_currentVehicle.isAutoEquipFull()
            shells = getAmmo(vehicle.shells)
        self.as_setAmmoS(shells, stateWarning)
        self.as_setModulesEnabledS(True)
        self.as_setVehicleHasTurretS(vehicle.hasTurrets)
        self.as_setDataS({'devices': getFittingSlotsData(vehicle, HANGAR_FITTING_SLOTS, VoClass=HangarFittingSlotVO)})
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\hangar\AmmunitionPanel.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:46:58 St�edn� Evropa (letn� �as)
