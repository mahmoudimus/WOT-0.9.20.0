# 2017.08.29 21:48:42 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/genConsts/FITTING_TYPES.py
"""
This file was generated using the wgpygen.
Please, don't edit this file manually.
"""

class FITTING_TYPES(object):
    OPTIONAL_DEVICE = 'optionalDevice'
    EQUIPMENT = 'equipment'
    SHELL = 'shell'
    VEHICLE = 'vehicle'
    MODULE = 'module'
    ORDER = 'order'
    BOOSTER = 'battleBooster'
    STORE_SLOTS = [VEHICLE,
     MODULE,
     SHELL,
     OPTIONAL_DEVICE,
     EQUIPMENT,
     BOOSTER]
    ARTEFACT_SLOTS = [OPTIONAL_DEVICE, EQUIPMENT]
    VEHICLE_GUN = 'vehicleGun'
    VEHICLE_TURRET = 'vehicleTurret'
    VEHICLE_CHASSIS = 'vehicleChassis'
    VEHICLE_ENGINE = 'vehicleEngine'
    VEHICLE_RADIO = 'vehicleRadio'
    MANDATORY_SLOTS = [VEHICLE_GUN,
     VEHICLE_TURRET,
     VEHICLE_CHASSIS,
     VEHICLE_ENGINE,
     VEHICLE_RADIO]
    RESERVE_SLOT1 = 'reserveSlot1'
    RESERVE_SLOT2 = 'reserveSlot2'
    RESERVE_SLOT3 = 'reserveSlot3'
    RESERVES_SLOTS = [RESERVE_SLOT1, RESERVE_SLOT2, RESERVE_SLOT3]
    TARGET_OTHER = 'other'
    TARGET_HANGAR = 'hangar'
    TARGET_HANGAR_CANT_INSTALL = 'hangarCantInstall'
    TARGET_HANGAR_DUPLICATE = 'hangarDuplicate'
    TARGET_VEHICLE = 'vehicle'
    ITEM_TARGETS = [TARGET_OTHER,
     TARGET_HANGAR,
     TARGET_HANGAR_CANT_INSTALL,
     TARGET_VEHICLE]
    OPTIONAL_DEVICE_FITTING_ITEM_RENDERER = 'OptDevFittingItemRendererUI'
    GUN_TURRET_FITTING_ITEM_RENDERER = 'GunTurretFittingItemRendererUI'
    RESERVE_FITTING_ITEM_RENDERER = 'ReserveFittingItemRendererUI'
    ENGINE_CHASSIS_FITTING_ITEM_RENDERER = 'EngineChassisFittingItemRendererUI'
    RADIO_FITTING_ITEM_RENDERER = 'RadioFittingItemRendererUI'
    BOOSTER_FITTING_ITEM_RENDERER = 'BoosterFittingItemRendererUI'
    FITTING_RENDERERS = [OPTIONAL_DEVICE_FITTING_ITEM_RENDERER,
     GUN_TURRET_FITTING_ITEM_RENDERER,
     RESERVE_FITTING_ITEM_RENDERER,
     ENGINE_CHASSIS_FITTING_ITEM_RENDERER,
     RADIO_FITTING_ITEM_RENDERER,
     BOOSTER_FITTING_ITEM_RENDERER]
    OPTIONAL_DEVICE_RENDERER_DATA_CLASS_NAME = 'net.wg.gui.lobby.modulesPanel.data.OptionalDeviceVO'
    MODULE_FITTING_RENDERER_DATA_CLASS_NAME = 'net.wg.gui.lobby.modulesPanel.data.ModuleVO'
    BOOSTER_FITTING_RENDERER_DATA_CLASS_NAME = 'net.wg.gui.lobby.modulesPanel.data.BoosterFittingItemVO'
    FITTING_RENDERER_DATA_NAMES = [OPTIONAL_DEVICE_RENDERER_DATA_CLASS_NAME, MODULE_FITTING_RENDERER_DATA_CLASS_NAME, BOOSTER_FITTING_RENDERER_DATA_CLASS_NAME]
    HANGAR_POPOVER_TOP_MARGIN = 80
    VEHPREVIEW_POPOVER_MIN_AVAILABLE_HEIGHT = 575
    LARGE_POPOVER_WIDTH = 540
    MEDUIM_POPOVER_WIDTH = 500
    SHORT_POPOVER_WIDTH = 440
    RESERVE_POPOVER_WIDTH = 480
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\genConsts\FITTING_TYPES.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:42 St�edn� Evropa (letn� �as)
