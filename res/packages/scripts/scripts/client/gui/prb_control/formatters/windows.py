# 2017.08.29 21:45:44 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/prb_control/formatters/windows.py
from gui.Scaleform.locale.PREBATTLE import PREBATTLE
from gui.prb_control.entities.base.ctx import PrbAction
from gui.ranked_battles.constants import PRIME_TIME_STATUS
from gui.shared import actions
from gui.prb_control.settings import PREBATTLE_ACTION_NAME
from helpers import dependency
from helpers import time_utils
from skeletons.gui.game_control import IRankedBattlesController
from skeletons.gui.lobby_context import ILobbyContext

class SwitchPeripheryCtx(object):

    def __init__(self, isForbidden = True):
        super(SwitchPeripheryCtx, self).__init__()
        self.__isForbidden = isForbidden

    def getHeader(self):
        raise NotImplementedError

    def getDescription(self):
        raise NotImplementedError

    def getSelectServerLabel(self):
        raise NotImplementedError

    def getApplySwitchLabel(self):
        raise NotImplementedError

    def getExtraChainSteps(self):
        raise NotImplementedError

    def getUpdateTime(self):
        return 0

    def isPeripheryAvailable(self, peripheryID):
        if self.__isForbidden:
            return peripheryID not in self._getForbiddenPeripherieIDs()
        return peripheryID in self._getAllowedPeripherieIDs()

    def _getForbiddenPeripherieIDs(self):
        raise NotImplementedError

    def _getAllowedPeripherieIDs(self):
        raise NotImplementedError


class SwitchPeripheryFortCtx(SwitchPeripheryCtx):
    lobbyContext = dependency.descriptor(ILobbyContext)

    def getHeader(self):
        return PREBATTLE.SWITCHPERIPHERYWINDOW_FORT_HEADER

    def getDescription(self):
        return PREBATTLE.SWITCHPERIPHERYWINDOW_FORT_DESCRIPTION

    def getSelectServerLabel(self):
        return PREBATTLE.SWITCHPERIPHERYWINDOW_FORT_SELECTSERVERLABEL

    def getApplySwitchLabel(self):
        return PREBATTLE.SWITCHPERIPHERYWINDOW_FORT_APPLYSWITCHLABEL

    def getExtraChainSteps(self):
        return None

    def _getForbiddenPeripherieIDs(self):
        return self.lobbyContext.getServerSettings().getForbiddenSortiePeripheryIDs()


class SwitchPeripheryRankedCtx(SwitchPeripheryCtx):
    rankedController = dependency.descriptor(IRankedBattlesController)

    def __init__(self):
        super(SwitchPeripheryRankedCtx, self).__init__(False)

    def getHeader(self):
        return PREBATTLE.SWITCHPERIPHERYWINDOW_RANKED_HEADER

    def getDescription(self):
        return PREBATTLE.SWITCHPERIPHERYWINDOW_RANKED_DESCRIPTION

    def getSelectServerLabel(self):
        return PREBATTLE.SWITCHPERIPHERYWINDOW_RANKED_SELECTSERVERLABEL

    def getApplySwitchLabel(self):
        return PREBATTLE.SWITCHPERIPHERYWINDOW_RANKED_APPLYSWITCHLABEL

    def getExtraChainSteps(self):

        def onLobbyInit():
            actions.SelectPrb(PrbAction(PREBATTLE_ACTION_NAME.RANKED)).invoke()

        return [actions.OnLobbyInitedAction(onInited=onLobbyInit)]

    def isPeripheryAvailable(self, peripheryID):
        status, _ = self.rankedController.getPrimeTimeStatus(peripheryID)
        return status == PRIME_TIME_STATUS.AVAILABLE

    def getUpdateTime(self):
        timeLeftList = []
        currentSeason = self.rankedController.getCurrentSeason()
        if currentSeason is None:
            return 0
        currentTime = time_utils.getCurrentLocalServerTimestamp()
        endTime = currentSeason.getCycleEndDate()
        for primeTime in self.rankedController.getPrimeTimes().itervalues():
            _, timeLeft = primeTime.getAvailability(currentTime, endTime)
            if timeLeft > 0:
                timeLeftList.append(timeLeft)

        if timeLeftList:
            return min(timeLeftList)
        else:
            return 0
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\formatters\windows.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:45:44 St�edn� Evropa (letn� �as)
