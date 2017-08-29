# 2017.08.29 21:43:56 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/bootcamp/states/StateResultScreen.py
from adisp import process
from copy import deepcopy
from bootcamp.BootCampEvents import g_bootcampEvents
from bootcamp.states import STATE
from bootcamp.states.AbstractState import AbstractState
from constants import BOOTCAMP_BATTLE_RESULT_MESSAGE
from gui.shared.items_cache import CACHE_SYNC_REASON
from bootcamp.BootcampTransition import BootcampTransition
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from skeletons.gui.battle_results import IBattleResultsService

class StateResultScreen(AbstractState):

    def __init__(self, lessonResults):
        super(StateResultScreen, self).__init__(STATE.RESULT_SCREEN)
        self.__lessonResults = deepcopy(lessonResults)

    def handleKeyEvent(self, event):
        pass

    @process
    def _doActivate(self):
        from bootcamp.Bootcamp import g_bootcamp
        from gui.battle_results.context import RequestResultsContext
        from bootcamp.BattleResultTransition import BattleResultTransition
        from gui.shared.personality import ServicesLocator
        sessionProvider = dependency.instance(IBattleSessionProvider)
        battleResultProvider = dependency.instance(IBattleResultsService)
        battleCtx = sessionProvider.getCtx()
        g_bootcamp.showActionWaitWindow()
        yield ServicesLocator.itemsCache.update(CACHE_SYNC_REASON.SHOW_GUI)
        g_bootcamp.hideActionWaitWindow()
        resultType, _, _, _, _ = g_bootcamp.getBattleResults()
        if resultType == BOOTCAMP_BATTLE_RESULT_MESSAGE.FAILURE:
            BootcampTransition.stop()
            g_bootcampEvents.onResultScreenFinished(0)
            return
        else:
            if battleCtx.lastArenaUniqueID:
                if g_bootcamp.transitionFlash is not None:
                    g_bootcamp.transitionFlash.close()
                g_bootcamp.transitionFlash = BattleResultTransition()
                g_bootcamp.transitionFlash.active(True)
                yield battleResultProvider.requestResults(RequestResultsContext(battleCtx.lastArenaUniqueID))
                battleCtx.lastArenaUniqueID = None
            return

    def _doDeactivate(self):
        pass
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\bootcamp\states\StateResultScreen.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:43:56 St�edn� Evropa (letn� �as)
