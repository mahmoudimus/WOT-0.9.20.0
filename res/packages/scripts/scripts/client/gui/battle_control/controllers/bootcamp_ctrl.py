# 2017.08.29 21:44:30 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/battle_control/controllers/bootcamp_ctrl.py
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController
from helpers import dependency
from skeletons.gui.game_control import IGameSessionController
from bootcamp.BootCampEvents import g_bootcampEvents

class BootcampController(IArenaVehiclesController):
    gameSession = dependency.descriptor(IGameSessionController)

    def __init__(self):
        super(BootcampController, self).__init__()

    def getControllerID(self):
        return None

    def arenaLoadCompleted(self):
        g_bootcampEvents.onArenaLoadCompleted()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\battle_control\controllers\bootcamp_ctrl.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:44:30 Støední Evropa (letní èas)
