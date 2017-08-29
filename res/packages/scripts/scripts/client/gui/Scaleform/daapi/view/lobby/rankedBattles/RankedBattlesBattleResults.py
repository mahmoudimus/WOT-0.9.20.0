# 2017.08.29 21:47:27 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/rankedBattles/RankedBattlesBattleResults.py
from gui.Scaleform.daapi.view.meta.RankedBattlesBattleResultsMeta import RankedBattlesBattleResultsMeta
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES
from gui.shared import event_dispatcher
from helpers import dependency
from skeletons.gui.game_control import IRankedBattlesController

class RankedBattlesBattleResults(RankedBattlesBattleResultsMeta):
    rankedController = dependency.descriptor(IRankedBattlesController)

    def __init__(self, ctx = None):
        super(RankedBattlesBattleResults, self).__init__()
        raise 'rankedResultsVO' in ctx or AssertionError
        self.__rankedResultsVO = ctx['rankedResultsVO']
        raise 'vehicle' in ctx or AssertionError
        self.__vehicle = ctx['vehicle']
        if not 'rankInfo' in ctx:
            raise AssertionError
            self.__rankInfo = ctx['rankInfo']
            accProgress = (self.__rankInfo.accRank, self.__rankInfo.accStep)
            vehProgress = (self.__rankInfo.vehRank, self.__rankInfo.vehStep)
            prevAccProgress, prevVehProgress = self.rankedController.getPrevRanks(accProgress, vehProgress, self.__rankInfo.stepChanges)
            maxProgress = max(accProgress, prevAccProgress)
            self.__ranks = self.rankedController.buildRanksChain(accProgress, maxProgress, prevAccProgress)
            self.__finalRanks = self.rankedController.buildRanksChain(accProgress, maxProgress, accProgress)
            accRanksCount = self.rankedController.getAccRanksTotal()
            self.__rankInfo.accRank < accRanksCount and self.__setRanks(accProgress, prevAccProgress)
        else:
            maxVehProgress = max(vehProgress, prevVehProgress)
            vehRanks = self.rankedController.buildVehicleRanksChain(vehProgress, maxVehProgress, prevVehProgress, self.__vehicle)
            self.__ranks.extend(vehRanks)
            vehFinalRanks = self.rankedController.buildVehicleRanksChain(vehProgress, maxVehProgress, vehProgress, self.__vehicle)
            self.__finalRanks.extend(vehFinalRanks)
            self.__setRanks(vehProgress, prevVehProgress, accRanksCount)

    def onEscapePress(self):
        self.__close()

    def onWindowClose(self):
        self.__close()

    def closeView(self):
        self.__close()

    def ready(self):
        self.__close()

    @property
    def rankedWidget(self):
        """
        This is small widget in the top of window, after animation is finished.
        :return: instance of the component. It is related only to this view
        """
        return self.getComponent(RANKEDBATTLES_ALIASES.RANKED_BATTLE_RESULTS_WIDGET)

    @property
    def rankedFinalWidget(self):
        """
        This is a big widget with animation of Rank/Step changes.
        :return: instance of the component. It is related only to this view
        """
        return self.getComponent(RANKEDBATTLES_ALIASES.RANKED_BATTLE_RESULTS_FINAL_WIDGET)

    def _populate(self):
        super(RankedBattlesBattleResults, self)._populate()
        self.__updateRankedWidget()
        self.__updateRankedFinalWidget()
        self.as_setDataS(self.__rankedResultsVO)

    def __setRanks(self, progress, prevProgress, adjustment = 0):
        rankID, _ = progress
        lastRankID, _ = prevProgress
        rankID += adjustment
        lastRankID += adjustment
        self.__currentRank = self.__ranks[rankID]
        self.__lastRank = self.__ranks[lastRankID]
        self.__currentFinalRank = self.__finalRanks[rankID]
        self.__lastFinalRank = self.__finalRanks[lastRankID]

    def __updateRankedWidget(self):
        if self.rankedWidget is not None:
            self.rankedWidget.update(self.__ranks, self.__currentRank, self.__lastRank)
        return

    def __updateRankedFinalWidget(self):
        if self.rankedFinalWidget is not None:
            self.rankedFinalWidget.update(self.__finalRanks, self.__currentFinalRank, self.__lastFinalRank)
        return

    def __close(self):
        self.destroy()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\rankedBattles\RankedBattlesBattleResults.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:47:27 St�edn� Evropa (letn� �as)
