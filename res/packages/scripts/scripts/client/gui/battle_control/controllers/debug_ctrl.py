# 2017.08.29 21:44:30 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/battle_control/controllers/debug_ctrl.py
import BigWorld
import BattleReplay
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from gui.battle_control.view_components import IViewComponentsController
from gui.shared.utils.TimeInterval import TimeInterval
from helpers import dependency
from skeletons.helpers.statistics import IStatisticsCollector
_UPDATE_INTERVAL = 0.2
_LATENCY_UNAVAILABLE = (0, 0, 0, 0)

class IDebugPanel(object):

    def updateDebugInfo(self, ping, fps, isLaggingNow, fpsReplay = -1):
        raise NotImplementedError


class DebugController(IViewComponentsController):
    """Controller for the debug panel.
    
    This class starts internal update cycle and updates debug panel.
    In order to collect lagging info from near vehicles, these vehicle's ids
    should be provided from outside using special methods.
    """
    statsCollector = dependency.descriptor(IStatisticsCollector)

    def __init__(self):
        super(DebugController, self).__init__()
        self._debugPanelUI = None
        self._timeInterval = None
        return

    def getControllerID(self):
        return BATTLE_CTRL_ID.DEBUG

    def startControl(self):
        self._timeInterval = TimeInterval(_UPDATE_INTERVAL, self, '_update')
        self._timeInterval.start()

    def stopControl(self):
        self._timeInterval.stop()
        self._timeInterval = None
        self.clearViewComponents()
        return

    def setViewComponents(self, debugPanelUI):
        raise isinstance(debugPanelUI, IDebugPanel) or AssertionError
        self._debugPanelUI = debugPanelUI

    def clearViewComponents(self):
        self._debugPanelUI = None
        return

    def _update(self):
        replayCtrl = BattleReplay.g_replayCtrl
        if replayCtrl.isPlaying and not replayCtrl.isBattleSimulation and replayCtrl.fps > 0:
            fps = BigWorld.getFPS()[1]
            fpsReplay = int(replayCtrl.fps)
            ping = replayCtrl.ping
            isLaggingNow = replayCtrl.isLaggingNow
        else:
            fpsReplay = -1
            isLaggingNow = BigWorld.statLagDetected()
            ping = BigWorld.statPing()
            fps = BigWorld.getFPS()[1]
            self.statsCollector.update()
            if replayCtrl.isRecording:
                replayCtrl.setFpsPingLag(fps, ping, isLaggingNow)
        try:
            ping = int(ping)
            fps = int(fps)
        except (ValueError, OverflowError):
            return

        if self._debugPanelUI is not None:
            self._debugPanelUI.updateDebugInfo(int(ping), int(fps), isLaggingNow, fpsReplay=fpsReplay)
        return
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\battle_control\controllers\debug_ctrl.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:44:31 St�edn� Evropa (letn� �as)
