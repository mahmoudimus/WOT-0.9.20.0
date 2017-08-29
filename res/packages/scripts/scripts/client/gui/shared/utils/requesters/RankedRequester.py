# 2017.08.29 21:50:20 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/utils/requesters/RankedRequester.py
import BigWorld
from adisp import async
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IRankedRequester

class RankedRequester(AbstractSyncDataRequester, IRankedRequester):
    """
    Requester for data of ranked battles.
    """

    @property
    def accRank(self):
        """
        Current account rank.
        :return: (currentRank, currentStep)
        """
        return self.getCacheValue('accRank', (0, 0))

    @property
    def vehRanks(self):
        """
        Current vehicles ranks.
        :return: {vehTypeCompDescr: (rank, step)}
        """
        return self.getCacheValue('vehRanks', {})

    @property
    def clientRank(self):
        """
        Last rank for which client animation was shown.
        :return: (currentRank, currentStep)
        """
        return self.getCacheValue('clientRank', (0, 0))

    @property
    def clientVehRanks(self):
        """
        Last vehicle rank for which client animation was shown.
        :return: {vehTypeCompDescr: (rank, step)}
        """
        return self.getCacheValue('clientVehRanks', {})

    @property
    def season(self):
        """
        Current season stamp.
        :return: (seasonID, cycleID)
        """
        return self.getCacheValue('season', (-1, -1))

    @property
    def badges(self):
        """
        List of player badges currently selected for display.
        :return: (badgeID, ...)
        """
        return map(str, self.getCacheValue('badges', ()))

    @property
    def maxRank(self):
        """
        Maximum achieved rank and step
        :return: (rankNumber, stepNumber)
        """
        return self.getCacheValue('maxRank', (0, 0))

    @property
    def maxVehRanks(self):
        """
        Max vehicles ranks.
        :return: {vehTypeCompDescr: (rank, step)}
        """
        return self.getCacheValue('maxVehRanks', {})

    @property
    def ladderPoints(self):
        """
        Ladder points earned in current cycle
        """
        return self.getCacheValue('ladderPts', 0)

    @property
    def seasonLadderPts(self):
        """
        Ladder points earned in current season
        """
        return self.getCacheValue('seasonLadderPts', 0)

    @property
    def stepsCount(self):
        """
        Steps count in current cycle
        """
        return self.getCacheValue('stepsCount', 0)

    @property
    def seasonStepsCount(self):
        """
        Steps count in current season
        """
        return self.getCacheValue('seasonStepsCount', 0)

    @property
    def maxRankWithAwardReceived(self):
        """
        Returns max rank for which award window was shown
        """
        return self.getCacheValue('clientMaxRank', (0, 0))

    @async
    def _requestCache(self, callback):
        BigWorld.player().ranked.getCache(lambda resID, value: self._response(resID, value, callback))

    def _preprocessValidData(self, data):
        if 'ranked' in data:
            return dict(data['ranked'])
        return dict()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\utils\requesters\RankedRequester.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:50:20 Støední Evropa (letní èas)
