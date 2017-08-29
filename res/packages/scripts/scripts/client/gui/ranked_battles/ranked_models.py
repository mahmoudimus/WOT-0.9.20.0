# 2017.08.29 21:45:48 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/ranked_battles/ranked_models.py
import operator
from collections import namedtuple
from operator import attrgetter
from gui.Scaleform.locale.RANKED_BATTLES import RANKED_BATTLES
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.ranked_battles.constants import RANK_TYPES
from gui.shared.formatters import text_styles
from gui.shared.money import Currency
from helpers import i18n
from helpers import time_utils
from shared_utils import CONST_CONTAINER, collapseIntervals, findFirst, first

class RANK_STATE(CONST_CONTAINER):
    UNDEFINED = 2
    NOT_ACQUIRED = 2
    ACQUIRED = 4
    LOST = 8
    MAXIMUM = 16
    UNBURNABLE = 32
    CURRENT = 64
    NEW_FOR_PLAYER = 128
    LAST_SEEN_BY_PLAYER = 256


class RANK_STATUS(CONST_CONTAINER):
    NOT_ACHIEVED = 'not_achieved'
    ACHIEVED = 'achieved'
    LOST = 'lost'


class CYCLE_STATUS(CONST_CONTAINER):
    PAST = 'past'
    CURRENT = 'current'
    FUTURE = 'future'


class RANK_CHANGE_STATES(object):
    RANK_EARNED = 'rankEarned'
    RANK_LOST = 'rankLost'
    STEP_EARNED = 'stepEarned'
    STEP_LOST = 'stepLost'
    NOTHING_CHANGED = 'nothingChanged'


class RankedCycle(namedtuple('RankedCycle', 'ID, status, startDate, endDate, ordinalNumber, points')):

    def __cmp__(self, other):
        raise isinstance(other, RankedCycle) or AssertionError
        return cmp(self.ID, other.ID)


class RankedSeason(object):
    """
    Wrapper for raw data from server, presenting info about season and its cycles
    """

    def __init__(self, seasonInfo, seasonData, stats = None, points = 0):
        self.__cycleStartDate, self.__cycleEndDate, self.__seasonId, self.__cycleID = seasonInfo
        self.__data = seasonData
        self.__cycles = None
        self.__stats = stats or {}
        self.__currCyclePoints = points
        return

    def getSeasonID(self):
        return self.__seasonId

    def getCycleID(self):
        return self.__cycleID

    def getStartDate(self):
        return self.__data['startSeason']

    def getEndDate(self):
        return self.__data['endSeason']

    def getAllCycles(self):
        if self.__cycles is None:
            self.__buildCycles()
        return self.__cycles

    def getCycleInfo(self):
        return self.getAllCycles()[self.getCycleID()]

    def getCycleStartDate(self):
        return self.__cycleStartDate

    def getCycleEndDate(self):
        return self.__cycleEndDate

    def getCycleOrdinalNumber(self):
        """
        @return: ordinal number of current cycle (starting from 1) or 0 if not presented
        """
        return self.getCycleInfo().ordinalNumber

    def getPassedCyclesNumber(self):
        """
        Iterate through cycles to calculate the number of passed cycles.
        :return: the number of passed cycles (int)
        """
        return sum((1 for cycle in self.getAllCycles().values() if cycle.status == CYCLE_STATUS.PAST))

    def getNumber(self):
        return self.__data.get('number')

    def getUserName(self):
        return i18n.makeString(RANKED_BATTLES.season_name(self.getNumber()))

    def getPoints(self):
        """
        @return: total points for season
        """
        dossierData = self.__stats.get((self.__seasonId, 0))
        if dossierData:
            _, _, _, points, _ = dossierData
        else:
            points = sum(map(attrgetter('points'), self.getAllCycles().values()))
        return points

    def __buildCycles(self):
        cycles = self.__data.get('cycles', {})
        currID = self.getCycleID()
        self.__cycles = {}
        for number, idx in enumerate(sorted(cycles.keys()), 1):
            cycleRawData = cycles[idx]
            points = 0
            if idx < currID or currID is None:
                status = CYCLE_STATUS.PAST
                cycleStats = self.__stats.get((self.__seasonId, idx))
                if cycleStats is not None:
                    _, _, _, points, _ = cycleStats
            elif idx == currID:
                status = CYCLE_STATUS.CURRENT
                points = self.__currCyclePoints
            else:
                status = CYCLE_STATUS.FUTURE
            self.__cycles[idx] = RankedCycle(idx, status, cycleRawData['start'], cycleRawData['end'], number, points)

        return


class RankStep(object):

    def __init__(self, stepID, stepState):
        super(RankStep, self).__init__()
        self._stepID = stepID
        self._state = stepState

    def getID(self):
        return self._stepID

    def canBeLost(self):
        return self._state & RANK_STATE.UNBURNABLE == 0

    def isAcquired(self):
        return self._state & RANK_STATE.ACQUIRED > 0

    def isLost(self):
        return self._state & RANK_STATE.LOST > 0

    def isNewForPlayer(self):
        return self._state & RANK_STATE.NEW_FOR_PLAYER > 0

    def isLastSeenByPlayer(self):
        return self._state & RANK_STATE.LAST_SEEN_BY_PLAYER > 0

    def isCurrent(self):
        return self._state & RANK_STATE.CURRENT > 0

    def isMax(self):
        return self._state & RANK_STATE.MAXIMUM > 0


class RankProgress(object):

    def __init__(self, steps):
        super(RankProgress, self).__init__()
        self._steps = steps

    def __eq__(self, other):
        if not isinstance(other, RankProgress):
            raise AssertionError
            if len(self.getSteps()) != len(other.getSteps()):
                return False
            return len(self.getAcquiredSteps()) != len(other.getAcquiredSteps()) and False
        return True

    def __ne__(self, other):
        raise isinstance(other, RankProgress) or AssertionError
        return not self.__eq__(other)

    def getSteps(self):
        return self._steps

    def getAcquiredSteps(self):
        return filter(operator.methodcaller('isAcquired'), self._steps)

    def getUserStr(self):
        return text_styles.main(' / '.join((text_styles.stats(len(self.getAcquiredSteps())), str(len(self.getSteps())))))

    def getNewUserStr(self):
        stepsSeenByPlayer = filter(lambda s: not s.isNewForPlayer(), self.getSteps())
        return text_styles.main(' / '.join((text_styles.stats(len(stepsSeenByPlayer)), str(len(self.getSteps())))))


class Rank(object):
    _ICON_SIZES = {'tiny': '24x24',
     'small': '58x80',
     'medium': '80x110',
     'big': '114x160',
     'huge': '190x260'}
    _awardsOrder = ['oneof',
     Currency.CRYSTAL,
     Currency.GOLD,
     'premium',
     Currency.CREDITS,
     'items']

    def __init__(self, rankID, rankState, points, progress = None, quest = None, finalQuest = None):
        super(Rank, self).__init__()
        self._rankID = rankID
        self._state = rankState
        self._progress = progress
        self._quest = quest
        self._type = RANK_TYPES.ACCOUNT
        self.__points = points
        self.__finalQuest = finalQuest

    def __eq__(self, other):
        if not isinstance(other, Rank):
            raise AssertionError
            if self.getID() != other.getID():
                return False
            return self.getProgress() != other.getProgress() and False
        return True

    def __ne__(self, other):
        raise isinstance(other, Rank) or AssertionError
        return not self.__eq__(other)

    def getType(self):
        return self._type

    def getID(self):
        return self._rankID

    def getUserName(self):
        return i18n.makeString(RANKED_BATTLES.rank_name(self._rankID))

    def getIcon(self, size):
        return RES_ICONS.getRankIcon(self._ICON_SIZES.get(size, ''), self._rankID)

    def getCycleFinalQuest(self):
        return self.__finalQuest

    def canBeLost(self):
        return self._state & RANK_STATE.UNBURNABLE == 0

    def isAcquired(self):
        return self._state & RANK_STATE.ACQUIRED > 0

    def isLost(self):
        return self._state & RANK_STATE.LOST > 0

    def isNewForPlayer(self):
        return self._state & RANK_STATE.NEW_FOR_PLAYER > 0

    def isLastSeenByPlayer(self):
        return self._state & RANK_STATE.LAST_SEEN_BY_PLAYER > 0

    def isCurrent(self):
        return self._state & RANK_STATE.CURRENT > 0

    def isMax(self):
        return self._state & RANK_STATE.MAXIMUM > 0

    def isRewardClaimed(self):
        """
        Check whether user has seen awards for this rank.
        It is possible to re-achieve a rank without getting the same awards again.
        IMPORTANT: Server will complete the quest itself if the user watches the match till the end and
                   returned to Hangar after battle. But if the user leaves the match, client's RankedBattlesController
                   will complete the quest (after user clicks to receive awards).
        :return: True if quest is NOT associated with this rank or the associated quest is completed, False otherwise.
        """
        return self._quest is None or self._quest.isCompleted()

    def hasProgress(self):
        return self._progress is not None and len(self._progress.getAcquiredSteps()) > 0

    def getProgress(self):
        return self._progress

    def getStatus(self):
        if self.isAcquired():
            return RANK_STATUS.ACHIEVED
        if self.isLost():
            return RANK_STATUS.LOST
        return RANK_STATUS.NOT_ACHIEVED

    def getQuest(self):
        return self._quest

    def getStepsCountToAchieve(self):
        return len(self.getProgress().getSteps())

    def getPoints(self):
        return self.__points

    def getAwardsVOs(self, forCycleFinish = False, iconSize = 'small'):
        if not isinstance(forCycleFinish, bool):
            raise AssertionError
            quest = self.__finalQuest if forCycleFinish else self._quest
            awards = []
            bonuses = quest is not None and {b.getName():b for b in quest.getBonuses()}
            for bonusName in self._awardsOrder:
                bonus = bonuses.pop(bonusName, None)
                if bonus:
                    awards.extend(bonus.getRankedAwardVOs(iconSize))

            for bonus in bonuses.values():
                awards.extend(bonus.getRankedAwardVOs(iconSize))

        return awards

    def getBoxIcon(self, size = '450x400', boxType = 'wooden', isOpened = True):
        return RES_ICONS.getRankedBoxIcon(size, boxType, '_opened' if isOpened else '', self._rankID)


class VehicleRank(Rank):

    def __init__(self, vehicle, accTopRankID, rankID, rankState, points, progress = None, quest = None):
        super(VehicleRank, self).__init__(rankID, rankState, points, progress, quest)
        self._type = RANK_TYPES.VEHICLE
        self.__vehicle = vehicle
        self.__accTopRankID = accTopRankID

    def getID(self):
        return self.getSerialID() + self.__accTopRankID

    def getSerialID(self):
        return self._rankID

    def getIcon(self, size):
        return RES_ICONS.getRankIcon(self._ICON_SIZES.get(size, ''), 'VehMaster')

    def getBoxIcon(self, size = '450x400', boxType = 'wooden', isOpened = True):
        return RES_ICONS.getRankedBoxIcon(size, boxType, '_opened' if isOpened else '', self.__accTopRankID)

    def getUserName(self):
        if self.getSerialID() > 1:
            nameKey = RANKED_BATTLES.RANKEDBATTLEVIEW_PROGRESSBLOCK_VEHICLEBONUSRANK
        else:
            nameKey = RANKED_BATTLES.RANKEDBATTLEVIEW_PROGRESSBLOCK_VEHICLERANK
        return i18n.makeString(nameKey, vehicle=self.__vehicle.shortUserName)

    def isRewardClaimed(self):
        return self.isAcquired()

    def getVehicle(self):
        return self.__vehicle


class PostBattleRankInfo(namedtuple('PostBattleRankInfo', ('accRank', 'accStep', 'vehRank', 'vehStep', 'stepChanges'))):

    @classmethod
    def fromDict(cls, dictWithInfo):
        accRank, accStep = dictWithInfo.get('accRank', (0, 0))
        vehRank, vehStep = dictWithInfo.get('vehRank', (0, 0))
        stepChanges = dictWithInfo.get('rankChange', 0)
        return cls(accRank, accStep, vehRank, vehStep, stepChanges)


class PrimeTime(object):

    def __init__(self, peripheryID, periods = None):
        super(PrimeTime, self).__init__()
        self.__peripheryID = peripheryID
        self.__periods = periods or {}

    def hasAnyPeriods(self):
        return bool(self.__periods)

    def getAvailability(self, forTime, cycleEnd):
        """
        Get availability for given time and cycle end for that time
        :param forTime: time stamp in UTC
        :param cycleEnd: cycle end time stamp in UTC
        :return: (is available that time, seconds left til end/start)
        """
        periods = self.getPeriodsBetween(forTime, cycleEnd)
        if periods:
            periodsIter = iter(periods)
            currentPeriod = findFirst(lambda (pS, pE): pS <= forTime < pE, periodsIter)
            if currentPeriod is not None:
                _, currentPeriodEnd = currentPeriod
                return (True, currentPeriodEnd - forTime)
            nextPeriod = first(periods)
            if nextPeriod is not None:
                nextPeriodStart, _ = nextPeriod
                return (False, nextPeriodStart - forTime)
        return (False, 0)

    def getPeriodsBetween(self, startTime, endTime):
        """
        Return the periods that includes two timestamps
        :param startTime: start time stamp in UTC
        :param endTime: end time stamp in UTC
        :return: list on periods as (start, end)
        """
        periods = []
        startDateTime = time_utils.getDateTimeInUTC(startTime)
        startTimeDayStart, _ = time_utils.getDayTimeBoundsForUTC(startTime)
        weekDay = startDateTime.isoweekday()
        while startTimeDayStart <= endTime:
            if weekDay in self.__periods:
                for (startH, startM), (endH, endM) in self.__periods[weekDay]:
                    periodStartTime = startTimeDayStart + startH * time_utils.ONE_HOUR + startM * time_utils.ONE_MINUTE
                    periodEndTime = startTimeDayStart + endH * time_utils.ONE_HOUR + endM * time_utils.ONE_MINUTE
                    if startTime < periodEndTime and periodStartTime <= endTime:
                        periods.append((max(startTime, periodStartTime), min(endTime, periodEndTime)))

            if weekDay == time_utils.WEEK_END:
                weekDay = time_utils.WEEK_START
            else:
                weekDay += 1
            startTimeDayStart += time_utils.ONE_DAY

        return collapseIntervals(periods)


class RankedDossier(namedtuple('RankedDossier', 'rank, step, vehRankCount, ladderPts, allStepsCount')):

    @staticmethod
    def defaults():
        return (0, 0, 0, 0, 0)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\ranked_battles\ranked_models.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:45:48 St�edn� Evropa (letn� �as)
