# 2017.08.29 21:46:11 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/crosshair/settings.py
from AvatarInputHandler import aih_constants
from gui.Scaleform.genConsts.ROOT_SWF_CONSTANTS import ROOT_SWF_CONSTANTS
CROSSHAIR_CONTAINER_SWF = 'battleCrosshairsApp.swf'
CROSSHAIR_ROOT_PATH = 'root.main'
CROSSHAIR_INIT_CALLBACK = ROOT_SWF_CONSTANTS.BATTLE_CROSSHAIRS_REGISTER_CALLBACK
CROSSHAIR_ITEM_PATH_FORMAT = '_level0.' + CROSSHAIR_ROOT_PATH + '.{}'
CROSSHAIR_RADIUS_MC_NAME = 'radiusMC'
SPG_GUN_MARKER_ELEMENTS_COUNT = aih_constants.SPG_GUN_MARKER_ELEMENTS_COUNT
SHOT_RESULT_TO_DEFAULT_COLOR = {aih_constants.SHOT_RESULT.UNDEFINED: 'normal',
 aih_constants.SHOT_RESULT.NOT_PIERCED: 'red',
 aih_constants.SHOT_RESULT.LITTLE_PIERCED: 'orange',
 aih_constants.SHOT_RESULT.GREAT_PIERCED: 'green'}
SHOT_RESULT_TO_ALT_COLOR = {aih_constants.SHOT_RESULT.UNDEFINED: 'normal',
 aih_constants.SHOT_RESULT.NOT_PIERCED: 'purple',
 aih_constants.SHOT_RESULT.LITTLE_PIERCED: 'yellow',
 aih_constants.SHOT_RESULT.GREAT_PIERCED: 'green'}
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\battle\shared\crosshair\settings.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:46:11 Støední Evropa (letní èas)
