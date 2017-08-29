# 2017.08.29 21:49:51 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/items_actions/factory.py
from debug_utils import LOG_ERROR
from gui.shared.gui_items.items_actions import actions
SELL_ITEM = 'sellItemAction'
BUY_VEHICLE = 'vehBuyAction'
BUY_MODULE = 'moduleBuyAction'
UNLOCK_ITEM = 'unlockAction'
INSTALL_ITEM = 'installItemAction'
BUY_AND_INSTALL_ITEM = 'buyAndInstallItemAction'
SET_VEHICLE_MODULE = 'setVehicleModuleAction'
SET_VEHICLE_LAYOUT = 'setVehicleLayoutAction'
BUY_AND_INSTALL_ITEM_VEHICLE_LAYOUT = 'buyAndInstallItemVehicleLayout'
_ACTION_MAP = {SELL_ITEM: actions.SellItemAction,
 UNLOCK_ITEM: actions.UnlockItemAction,
 BUY_MODULE: actions.ModuleBuyAction,
 BUY_VEHICLE: actions.VehicleBuyAction,
 INSTALL_ITEM: actions.InstallItemAction,
 BUY_AND_INSTALL_ITEM: actions.BuyAndInstallItemAction,
 SET_VEHICLE_MODULE: actions.SetVehicleModuleAction,
 SET_VEHICLE_LAYOUT: actions.SetVehicleLayoutAction,
 BUY_AND_INSTALL_ITEM_VEHICLE_LAYOUT: actions.BuyAndInstallItemVehicleLayout}

def doAction(actionType, *args, **kwargs):
    if actionType in _ACTION_MAP:
        skipConfirm = kwargs.get('skipConfirm', False)
        action = _ACTION_MAP[actionType](*args)
        action.skipConfirm = skipConfirm
        action.doAction()
    else:
        LOG_ERROR('Action type is not found', actionType)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\items_actions\factory.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:49:52 St�edn� Evropa (letn� �as)
