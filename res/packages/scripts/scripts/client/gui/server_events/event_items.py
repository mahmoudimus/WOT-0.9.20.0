# 2017.08.29 21:49:22 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/server_events/event_items.py
import operator
import time
from abc import ABCMeta
from collections import namedtuple
import constants
import nations
from debug_utils import LOG_CURRENT_EXCEPTION, LOG_ERROR
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK
from gui.Scaleform.locale.QUESTS import QUESTS
from gui.ranked_battles import ranked_helpers
from gui.server_events.bonuses import getBonusObj, compareBonuses, BoxBonus
from gui.server_events.formatters import isMarathon, getLinkedActionID
from gui.server_events.modifiers import getModifierObj, compareModifiers
from gui.server_events.parsers import AccountRequirements, VehicleRequirements, TokenQuestAccountRequirements, PreBattleConditions, PostBattleConditions, BonusConditions
from helpers import dependency
from helpers import getLocalizedData, i18n, time_utils
from potapov_quests import PQ_STATE as _PQS, PQ_BRANCH
from shared_utils import first, findFirst
from skeletons.gui.shared import IItemsCache
EventBattles = namedtuple('EventBattles', ['vehicleTags',
 'vehicles',
 'enabled',
 'arenaTypeID'])

class DEFAULTS_GROUPS(object):
    FOR_CURRENT_VEHICLE = 'currentlyAvailable'
    UNGROUPED_ACTIONS = 'ungroupedActions'
    UNGROUPED_QUESTS = 'ungroupedQuests'
    MOTIVE_QUESTS = 'motiveQuests'


class TOKEN_SHOP(object):
    """ Possible states of the token's sale availability.
    """
    SHOW = 'show'
    HIDE = 'hide'
    WEB = 'web'


class ServerEventAbstract(object):
    __metaclass__ = ABCMeta

    def __init__(self, eID, data):
        self._id = eID
        self._data = dict(data)
        self._groupID = None
        return

    def isGuiDisabled(self):
        return self._data.get('disableGui', False)

    def isHidden(self):
        return self._data.get('hidden', False)

    def getWeekDays(self):
        return self._data.get('weekDays', set())

    def getActiveTimeIntervals(self):
        if 'activeTimeIntervals' in self._data:
            return map(lambda (l, h): (l[0] * 3600 + l[1] * 60, h[0] * 3600 + h[1] * 60), self._data['activeTimeIntervals'])
        return []

    def getID(self):
        return self._id

    def getIconID(self):
        return self._data.get('uiDecoration', None)

    def setGroupID(self, groupID):
        self._groupID = groupID

    def getGroupID(self):
        return self._groupID

    def getPriority(self):
        return self._data.get('priority', 0)

    def getData(self):
        return self._data

    def getType(self):
        return self._data.get('type', 0)

    def getBattleTypeName(self):
        return 'random'

    def getStartTime(self):
        if 'startTime' in self._data:
            return time_utils.makeLocalServerTime(self._data['startTime'])
        return time.time()

    def getFinishTime(self):
        if 'finishTime' in self._data:
            return time_utils.makeLocalServerTime(self._data['finishTime'])
        return time.time()

    def getUserName(self):
        return getLocalizedData(self._data, 'name')

    def getDescription(self):
        return getLocalizedData(self._data, 'description')

    def getStartTimeLeft(self):
        return time_utils.getTimeDeltaFromNowInLocal(self.getStartTime())

    def getFinishTimeLeft(self):
        return time_utils.getTimeDeltaFromNowInLocal(self.getFinishTime())

    def isOutOfDate(self):
        return self.getFinishTimeLeft() <= 0

    def getUserType(self):
        return ''

    def isIGR(self):
        return self._data.get('isIGR', False)

    def isCompleted(self, progress = None):
        return False

    def isTokensOnSale(self):
        """ Returns true if tokens are always statically on sale, false otherwise.
        """
        state = self._getTokenSaleState()
        return state == TOKEN_SHOP.SHOW

    def isTokensOnSaleDynamic(self):
        """ Returns true if the state of tokens availability on shop is dynamic.
        """
        return self._getTokenSaleState() == TOKEN_SHOP.WEB

    def getNearestActivityTimeLeft(self):
        timeLeft = None
        if self.getStartTimeLeft() > 0:
            timeLeft = (self.getStartTimeLeft(), (0, time_utils.ONE_DAY))
        else:
            weekDays, timeIntervals = self.getWeekDays(), self.getActiveTimeIntervals()
            if len(weekDays) or len(timeIntervals):
                timeLeft = next(time_utils.ActivityIntervalsIterator(time_utils.getServerTimeCurrentDay(), time_utils.getServerRegionalWeekDay(), weekDays, timeIntervals))
        return timeLeft

    def hasPremIGRVehBonus(self):
        return False

    def isAvailable(self):
        if self.getStartTimeLeft() > 0:
            return (False, 'in_future')
        if self.isOutOfDate():
            return (False, 'out_of_date')
        weekDays = self.getWeekDays()
        if len(weekDays) and time_utils.getServerRegionalWeekDay() not in weekDays:
            return (False, 'invalid_weekday')
        intervals = self.getActiveTimeIntervals()
        serverTime = time_utils.getServerTimeCurrentDay()
        if intervals:
            for low, high in intervals:
                if low <= serverTime <= high:
                    break
            else:
                return (False, 'invalid_time_interval')

        if not self._checkConditions():
            return (False, 'requirements')
        return (True, '')

    def isAvailableForVehicle(self, vehicle):
        """ Check if quest is available for provided vehicle.
        """
        result, error = self.isAvailable()
        if result and not self._checkVehicleConditions(vehicle):
            return (False, 'requirement')
        return (result, error)

    def isValidVehicleCondition(self, vehicle):
        """
        Check if quest's vehicle condition is available for provided vehicle.
        """
        return self._checkVehicleConditions(vehicle)

    def getBonuses(self, bonusName = None, isCompensation = False):
        return []

    def getParents(self):
        return []

    def getParentsName(self):
        return []

    def _checkConditions(self):
        return True

    def _checkVehicleConditions(self, vehicle):
        """ Check conditions with relation to provided vehicle.
        """
        return True

    def _getTokenSaleState(self):
        return self._data.get('shopButton', TOKEN_SHOP.HIDE)

    def __repr__(self):
        return '%s(qID = %s, groupID = %s)' % (self.__class__.__name__, self._id, self._groupID)


class Group(ServerEventAbstract):

    def getGroupEvents(self):
        return self._data.get('groupContent', [])

    def getGroupContent(self, srvEvents):
        """ Isolate quests of the current group from the given events.
        """
        groupQuests = []
        for questID in self.getGroupEvents():
            quest = srvEvents.get(questID)
            if quest is not None:
                groupQuests.append(quest)

        return groupQuests

    def isMarathon(self):
        return isMarathon(self.getID())

    def getLinkedAction(self, actions):
        """
        Gets linked action ID
        """
        return getLinkedActionID(self.getID(), actions)

    def getMainQuest(self, events):
        """ Get marathon's main quest (quest with special prefix)
        """
        if not self.isMarathon():
            LOG_ERROR('Trying to find main quest in non-marathon group', self.getID())
            return None
        else:
            tokenQuests = []
            for quest in events:
                if isMarathon(quest.getID()):
                    return quest

            LOG_ERROR('There is no main token quest in the marathon', self.getID())
            return None

    def withManyTokenSources(self, svrEvents):
        uniqueTokens = set()
        uniqueChildren = set()
        for qID in self.getGroupEvents():
            quest = svrEvents.get(qID)
            if quest is not None:
                children = quest.getChildren()
                if len(children) > 0:
                    for key, value in children.iteritems():
                        uniqueChildren |= set(value)
                        uniqueTokens.add(key)

        return len(uniqueTokens) == 1 and len(uniqueChildren) > 1


class Quest(ServerEventAbstract):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, qID, data, progress = None):
        super(Quest, self).__init__(qID, data)
        self._progress = progress
        self._children, self._parents, self._parentsName = {}, {}, {}
        conds = dict(data['conditions'])
        preBattle = dict(conds['preBattle'])
        self.accountReqs = AccountRequirements(preBattle['account'])
        self.vehicleReqs = VehicleRequirements(preBattle['vehicle'])
        self.preBattleCond = PreBattleConditions(preBattle['battle'])
        self.bonusCond = BonusConditions(conds['common'], self.getProgressData(), self.preBattleCond)
        self.postBattleCond = PostBattleConditions(conds['postBattle'], self.preBattleCond)
        self._groupID = DEFAULTS_GROUPS.UNGROUPED_QUESTS
        self.__linkedActions = []

    def isCompensationPossible(self):
        return isMarathon(self.getGroupID()) and bool(self.getBonuses('tokens'))

    def isAvailable(self):
        if self.bonusCond.getBonusLimit() is not None and self.bonusCond.isDaily() and self.isCompleted():
            return (False, 'dailyComplete')
        else:
            return super(Quest, self).isAvailable()

    @property
    def linkedActions(self):
        return self.__linkedActions

    @linkedActions.setter
    def linkedActions(self, value):
        self.__linkedActions = value

    def getUserType(self):
        return i18n.makeString(QUESTS.ITEM_TYPE_QUEST)

    def getProgressExpiryTime(self):
        return self._data.get('progressExpiryTime', time.time())

    def isCompletedByGroup(self, groupByKey):
        bonusLimit = self.bonusCond.getBonusLimit()
        if bonusLimit is not None:
            if self.bonusCond.getGroupByValue() is None:
                return self.isCompleted()
            if self._progress is not None:
                return bonusLimit <= self.getBonusCount(groupByKey)
        return False

    def isCompleted(self, progress = None):
        progress = progress or self._progress
        bonusLimit = self.bonusCond.getBonusLimit()
        if bonusLimit is not None:
            groupBy = self.bonusCond.getGroupByValue()
            if groupBy is None:
                return self.getBonusCount(progress=progress) >= bonusLimit
            if progress is not None:
                if groupBy == 'nation':
                    return self.__checkGroupedCompletion(nations.AVAILABLE_NAMES, progress, bonusLimit)
                if groupBy == 'level':
                    return self.__checkGroupedCompletion(xrange(1, constants.MAX_VEHICLE_LEVEL + 1), progress, bonusLimit, keyMaker=lambda lvl: 'level %d' % lvl)
                if groupBy == 'class':
                    return self.__checkGroupedCompletion(constants.VEHICLE_CLASSES, progress, bonusLimit)
                if groupBy == 'vehicle':
                    pass
        return super(Quest, self).isCompleted()

    def setChildren(self, children):
        self._children = children

    def getChildren(self):
        return self._children

    def setParents(self, parents):
        self._parents = parents

    def getParents(self):
        return self._parents

    def setParentsName(self, parentsName):
        self._parentsName = parentsName

    def getParentsName(self):
        return self._parentsName

    def getBonusCount(self, groupByKey = None, progress = None):
        progress = progress or self._progress
        if progress is not None:
            groupBy = self.bonusCond.getGroupByValue()
            if groupBy is None:
                return progress.get(None, {}).get('bonusCount', 0)
            if groupByKey is not None:
                return progress.get(groupByKey, {}).get('bonusCount', 0)
            return sum((p.get('bonusCount', 0) for p in progress.itervalues()))
        else:
            return 0

    def getProgressData(self):
        return self._progress or {}

    def getBonuses(self, bonusName = None, isCompensation = False, bonusData = None):
        """ Get quest's bonuses.
        
        :param bonusName: str, bonus name to be find
        :param isCompensation: bool, treat returned bonuses as compensation
        :param bonusData: dict, formed quest bonus dict section, wrap bonus data for existing bonus dict
        :return: list with found bonuses
        """
        result = []
        bonusData = bonusData or self._data.get('bonus', {})
        if bonusName is None:
            for name, value in bonusData.iteritems():
                bonus = getBonusObj(self, name, value, isCompensation)
                if bonus is not None:
                    result.append(self._bonusDecorator(bonus))

        elif bonusName in bonusData:
            bonus = getBonusObj(self, bonusName, bonusData[bonusName], isCompensation)
            if bonus is not None:
                result.append(self._bonusDecorator(bonus))
        return sorted(result, cmp=compareBonuses, key=operator.methodcaller('getName'))

    def getCompensation(self):
        """ Get possible compensation for the token.
        
        This method is only makes sense for the compensation quest, i.e.
        a special token quest that consumes extra tokens and gives bonuses instead.
        
        This extra bonuses are needed in case of marathon, when the main token
        quest is already completed, but still player can complete battle quests
        and get some rewards.
        """
        compensatedToken = findFirst(lambda t: t.isDisplayable(), self.accountReqs.getTokens())
        if compensatedToken:
            return {compensatedToken.getID(): self.getBonuses(isCompensation=True)}
        else:
            return {}

    def hasPremIGRVehBonus(self):
        vehBonuses = self.getBonuses('vehicles')
        for vehBonus in vehBonuses:
            vehicles = vehBonus.getValue()
            for intCD, data in vehicles.iteritems():
                item = self.itemsCache.items.getItemByCD(intCD)
                if item.isPremiumIGR and data.get('rent', None) is not None:
                    return True

        return False

    def getSuitableVehicles(self):
        return self.vehicleReqs.getSuitableVehicles()

    def _bonusDecorator(self, bonus):
        """
            allows to do some additional bonus configuration when they are created in getBonuses.
            Originally is used in RankedQuest to set BoxBonus icon configuration
        """
        if self.getType() == constants.EVENT_TYPE.TOKEN_QUEST and bonus.getName() == 'oneof':
            if ranked_helpers.isRankedQuestID(self.getID()):
                _, cohort, _ = ranked_helpers.getRankedDataFromTokenQuestID(self.getID())
                bonus.setupIconHandler(BoxBonus.HANDLER_NAMES.RANKED, ('metal', cohort))
                bonus.setTooltipType('rankedSeason')
        return bonus

    def __checkGroupedCompletion(self, values, progress, bonusLimit = None, keyMaker = lambda v: v):
        bonusLimit = bonusLimit or self.bonusCond.getBonusLimit()
        for value in values:
            if bonusLimit > self.getBonusCount(groupByKey=keyMaker(value), progress=progress):
                return False

        return True

    def _checkConditions(self):
        if not self.accountReqs.isAvailable():
            return False
        else:
            return self.vehicleReqs.isAnyVehicleAcceptable() or self.vehicleReqs.getSuitableVehicles()

    def _checkVehicleConditions(self, vehicle):
        return self.vehicleReqs.isAnyVehicleAcceptable() or vehicle in self.vehicleReqs.getSuitableVehicles()


class TokenQuest(Quest):
    """ Quest without battle conditions (only consumes tokens from other quests).
    
    The key difference is that we don't check token requirements availability
    when checking overall quest availability (see WOTD-81694)
    """

    def __init__(self, qID, data, progress = None):
        super(TokenQuest, self).__init__(qID, data, progress)
        self.accountReqs = TokenQuestAccountRequirements(self.accountReqs.getSection())

    def _checkConditions(self):
        return self.accountReqs.isAvailable()


class PersonalQuest(Quest):

    def __init__(self, qID, data, progress = None, expiryTime = None):
        super(PersonalQuest, self).__init__(qID, data, progress)
        self.expiryTime = expiryTime

    def getFinishTime(self):
        if self.expiryTime is not None:
            return min(super(PersonalQuest, self).getFinishTime(), self.expiryTime)
        else:
            return super(PersonalQuest, self).getFinishTime()

    def getRequiredToken(self):
        return self._data.get('requiredToken', None)


class RankedQuest(Quest):
    boxIconSizes = {'big': '450x400',
     'small': '100x88'}

    def __init__(self, qID, data, progress = None):
        super(RankedQuest, self).__init__(qID, data, progress)
        self.__rankedData = self.__parseRankSeasonData(data)

    def getRank(self):
        return self.__rankedData.get('rank')

    def getSeasonID(self):
        return self.__rankedData.get('season')

    def getCycleID(self):
        return self.__rankedData.get('cycle')

    def isProcessedAtCycleEnd(self):
        return self.__rankedData['subtype'] == 'cycle'

    def isForVehicleMastering(self):
        return self.__rankedData['subtype'] == 'vehicle'

    def isForRank(self):
        return self.__rankedData['subtype'] == 'rank'

    def isBooby(self):
        return self.__rankedData['subtype'] == 'booby'

    def getBattleTypeName(self):
        return 'ranked'

    def _bonusDecorator(self, bonus):
        if bonus.getName() == 'oneof':
            if self.isProcessedAtCycleEnd():
                bonus.setupIconHandler(BoxBonus.HANDLER_NAMES.RANKED, ('wooden', self.getRank()))
                bonus.setTooltipType('rankedCycle')
        return bonus

    @classmethod
    def __parseRankSeasonData(cls, data):
        conditionsDict = cls.__dictMaker(data.get('conditions', {}))
        rankedData = conditionsDict.get('common', {})
        result = {}
        if rankedData:
            for key in ('season', 'cycle'):
                if key in rankedData:
                    result[key] = rankedData[key]['value']

            if 'maxRank' in rankedData:
                rank = rankedData['maxRank']
                if 'and' in rank:
                    rankBounds = rank['and']
                    result['rank'] = int(first(rankBounds.values())['value'])
                else:
                    result['rank'] = int(rank['greaterOrEqual']['value'])
        result['subtype'] = data.get('subtype')
        return result

    @classmethod
    def __dictMaker(cls, kVList):
        result = {}
        for key, value in dict(kVList).iteritems():
            if isinstance(value, (list, tuple)) and len(value):
                result[key] = cls.__dictMaker(value)
            else:
                result[key] = value

        return result


ActionData = namedtuple('ActionData', 'discountObj priority uiDecoration')

class Action(ServerEventAbstract):

    def __init__(self, qID, data):
        super(Action, self).__init__(qID, data)
        self._groupID = DEFAULTS_GROUPS.UNGROUPED_ACTIONS
        self.__linkedQuests = []

    @property
    def linkedQuests(self):
        return self.__linkedQuests

    @linkedQuests.setter
    def linkedQuests(self, value):
        self.__linkedQuests = value

    def getUserType(self):
        return i18n.makeString(QUESTS.ITEM_TYPE_ACTION)

    def getActions(self):
        result = {}
        for stepData in self._data.get('steps'):
            mName = stepData.get('name')
            priority = stepData.get('priority')
            params = stepData.get('params')
            uiDecoration = stepData.get('uiDecoration')
            m = getModifierObj(mName, params)
            if m is None:
                continue
            modifiers = m.splitModifiers()
            for modifier in modifiers:
                if mName in result:
                    result[mName].extend([ActionData(modifier, priority, uiDecoration)])
                else:
                    result[mName] = [ActionData(modifier, priority, uiDecoration)]

        return result

    def getModifiers(self):
        result = {}
        for stepData in self._data.get('steps'):
            mName = stepData.get('name')
            m = getModifierObj(mName, stepData.get('params'))
            if m is None:
                continue
            if mName in result:
                result[mName].update(m)
            else:
                result[mName] = m

        return sorted(result.itervalues(), key=operator.methodcaller('getName'), cmp=compareModifiers)


class PQSeason(object):

    def __init__(self, seasonID, info):
        self.__id = seasonID
        self.__info = info
        self.__tiles = {}
        self.__isUnlocked = False

    def getID(self):
        return self.__id

    def getName(self):
        return self.__info['name']

    def getUserName(self):
        return self.__info['userString']

    def getUserDescription(self):
        return self.__info['description']

    def getTiles(self):
        return self.__tiles

    def isUnlocked(self):
        return self.__isUnlocked

    def updateProgress(self):
        for tile in self.__tiles.itervalues():
            if tile.isUnlocked():
                self.__isUnlocked = True
                break

    def _addTile(self, tile):
        if tile.getID() not in self.__tiles:
            self.__tiles[tile.getID()] = tile


class PQTile(object):

    def __init__(self, tileID, info):
        self.__id = tileID
        self.__info = info
        self.__quests = {}
        self.__initialQuests = {}
        self.__finalQuests = {}
        self.__isUnlocked = False
        self.__achievements = dict(((chID, (ACHIEVEMENT_BLOCK.TOTAL, aName)) for chID, aName in self.__info['achievements'].iteritems()))
        self.__tokens = {}
        self.__bonuses = {}
        self.__isAwardAchieved = False

    def getID(self):
        return self.__id

    def getNextTileID(self):
        return self.__info['nextTileID']

    def getName(self):
        return self.__info['name']

    def getUserName(self):
        return self.__info['userString']

    def getUserDescription(self):
        return self.__info['description']

    def getChainVehicleClass(self, chainID):
        firstQuest = first(self.__quests.get(chainID, {}).itervalues())
        if firstQuest is not None:
            return first(firstQuest.getVehicleClasses())
        else:
            return

    def getChainMajorTag(self, chainID):
        firstQuest = first(self.__quests.get(chainID, {}).itervalues())
        if firstQuest is not None:
            return firstQuest.getMajorTag()
        else:
            return

    def getChainSortKey(self, chainID):
        return self.getChainMajorTag(chainID)

    def getChainTotalTokensCount(self, chainID, isMainBonuses = None):
        result = 0
        for q in self.__quests[chainID].itervalues():
            for tokenBonus in q.getBonuses('tokens', isMainBonuses):
                for token in tokenBonus.getTokens().itervalues():
                    result += token.count

        return result

    def getIconID(self):
        return self.__info['iconID']

    def getSeasonID(self):
        return self.__info['seasonID']

    def getChainSize(self):
        return self.__info['questsInChain']

    def getQuestsCount(self):
        return self.__info['chainsCount'] * self.getChainSize()

    def getPrice(self):
        return self.__info['price']

    def getQuests(self):
        return self.__quests

    def getQuestsInChainByFilter(self, chainID, filterFunc = lambda v: True):
        result = {}
        for qID, q in self.__quests[chainID].iteritems():
            if filterFunc(q):
                result[qID] = q

        return result

    def getQuestsByFilter(self, filterFunc = lambda v: True):
        result = {}
        for _, quests in self.__quests.iteritems():
            for qID, q in quests.iteritems():
                if filterFunc(q):
                    result[qID] = q

        return result

    def getInProgressQuests(self):
        return self.getQuestsByFilter(lambda quest: quest.isInProgress())

    def getCompletedQuests(self, isRewardReceived = None):
        return self.getQuestsByFilter(lambda quest: quest.isCompleted(isRewardReceived=isRewardReceived))

    def getFullCompletedQuests(self, isRewardReceived = None):
        return self.getQuestsByFilter(lambda quest: quest.isFullCompleted(isRewardReceived=isRewardReceived))

    def isCompleted(self, isRewardReceived = None):
        return len(self.getCompletedQuests(isRewardReceived)) == self.getQuestsCount()

    def isInProgress(self):
        return len(self.getInProgressQuests()) > 0

    def isFullCompleted(self, isRewardReceived = None):
        return len(self.getFullCompletedQuests(isRewardReceived)) == self.getQuestsCount()

    def isAwardAchieved(self):
        return self.__isAwardAchieved

    def getCompletedFinalQuests(self, isRewardReceived = None):
        return self.getQuestsByFilter(lambda quest: quest.isCompleted(isRewardReceived=isRewardReceived) and quest.isFinal())

    def getInitialQuests(self):
        return self.__initialQuests

    def getFinalQuests(self):
        return self.__finalQuests

    def isUnlocked(self):
        return self.__isUnlocked

    def getAchievements(self):
        return self.__achievements

    def getTokens(self):
        return self.__tokens

    def getTokensCount(self):
        return tuple((sum(map(operator.itemgetter(i), self.__tokens.values())) for i in xrange(2)))

    def getTotalTokensCount(self):
        result = 0
        for chainID in self.__quests.iterkeys():
            result += self.getChainTotalTokensCount(chainID)

        return result

    def getBonuses(self):
        return self.__bonuses

    def getVehicleBonus(self):
        for bonuses in self.getBonuses().itervalues():
            for bonus in bonuses:
                if bonus.getName() == 'vehicles':
                    for vehicle, _ in bonus.getVehicles():
                        return vehicle

        return None

    def updateProgress(self, eventsCache):
        qp = eventsCache.questsProgress
        self.__isUnlocked = False
        for quest in self.__initialQuests.itervalues():
            if quest.isUnlocked():
                self.__isUnlocked = True
                break

        self.__tokens, self.__bonuses = {}, {}
        for quest in eventsCache.getHiddenQuests().itervalues():
            for token in quest.accountReqs.getTokens():
                if token.getID() in self.__info['tokens']:
                    self.__tokens[token.getID()] = (qp.getTokenCount(token.getID()), token.getNeededCount())
                    self.__bonuses.setdefault(token.getID(), []).extend(quest.getBonuses())

        def _getTokensFromBonuses(bonuses):
            result = 0
            for tokenBonus in bonuses:
                for t in tokenBonus.getTokens().itervalues():
                    result += t.count

            return result

        gottenTokensCount = 0
        for quests in self.__quests.itervalues():
            for q in quests.itervalues():
                if q.isMainCompleted(isRewardReceived=True):
                    gottenTokensCount += _getTokensFromBonuses(q.getBonuses('tokens', isMain=True))
                if q.isFullCompleted(isRewardReceived=True):
                    gottenTokensCount += _getTokensFromBonuses(q.getBonuses('tokens', isMain=False))

        _, neededTokensCount = self.getTokensCount()
        self.__isAwardAchieved = gottenTokensCount >= neededTokensCount

    def _addQuest(self, quest):
        questID = quest.getID()
        chain = self.__quests.setdefault(quest.getChainID(), {})
        if questID not in chain:
            chain[questID] = quest
            if quest.isInitial():
                self.__initialQuests[questID] = quest
            elif quest.isFinal():
                self.__finalQuests[questID] = quest


class PotapovQuest(Quest):

    def __init__(self, qID, pqType, pqProgress = None, seasonID = None):
        super(PotapovQuest, self).__init__(qID, pqType.mainQuestInfo)
        self.__pqType = pqType
        self.__pqProgress = pqProgress
        self.__seasonID = seasonID

    def getPQType(self):
        return self.__pqType

    def getMainQuestID(self):
        return self.__pqType.mainQuestInfo['id']

    def getAddQuestID(self):
        return self.__pqType.addQuestInfo['id']

    def getChainID(self):
        return self.__pqType.chainID

    def getTileID(self):
        return self.__pqType.tileID

    def setSeasonID(self, seasonID):
        self.__seasonID = seasonID

    def getSeasonID(self):
        return self.__seasonID

    def getUserType(self):
        return i18n.makeString('#quests:item/type/potapov')

    def getUserName(self):
        return self.__pqType.userString

    def getUserDescription(self):
        return self.__pqType.description

    def getUserAdvice(self):
        return self.__pqType.advice

    def getUserMainCondition(self):
        return self.__pqType.conditionMain

    def getUserAddCondition(self):
        return self.__pqType.conditionAdd

    def getVehMinLevel(self):
        return self.__pqType.minLevel

    def getQuestBranch(self):
        return self.__pqType.branch

    def getQuestBranchName(self):
        return PQ_BRANCH.TYPE_TO_NAME[self.getQuestBranch()]

    def isUnlocked(self):
        return self.__pqProgress is not None and self.__pqProgress.unlocked

    def isInProgress(self):
        return self.__pqProgress is not None and self.__pqProgress.selected and not self.needToGetReward()

    def isAvailableToPerform(self):
        return self.__pqProgress is not None and self.__pqProgress.unlocked and self.__pqProgress.state <= _PQS.UNLOCKED

    def hasProgress(self):
        return self.__pqProgress.state > _PQS.NONE

    def isInitial(self):
        return self.__pqType.isInitial

    def isFinal(self):
        return self.__pqType.isFinal

    def getVehicleClasses(self):
        return set(self.__pqType.vehClasses)

    def getMajorTag(self):
        return self.__pqType.getMajorTag()

    def isMainCompleted(self, isRewardReceived = None):
        if isRewardReceived is True:
            states = (_PQS.MAIN_REWARD_GOTTEN, _PQS.ALL_REWARDS_GOTTEN)
        elif isRewardReceived is False:
            states = (_PQS.NEED_GET_MAIN_REWARD, _PQS.NEED_GET_ALL_REWARDS)
        else:
            states = (_PQS.MAIN_REWARD_GOTTEN,
             _PQS.ALL_REWARDS_GOTTEN,
             _PQS.NEED_GET_MAIN_REWARD,
             _PQS.NEED_GET_ALL_REWARDS)
        return self.__checkForStates(*states)

    def isFullCompleted(self, isRewardReceived = None):
        if isRewardReceived is True:
            states = (_PQS.ALL_REWARDS_GOTTEN,)
        elif isRewardReceived is False:
            states = (_PQS.NEED_GET_ALL_REWARDS,)
        else:
            states = _PQS.COMPLETED
        return self.__checkForStates(*states)

    def isCompleted(self, progress = None, isRewardReceived = None):
        return self.isMainCompleted(isRewardReceived) or self.isFullCompleted(isRewardReceived)

    def canBeSelected(self):
        return self.isUnlocked() and not self.isFullCompleted() and not self.isInProgress()

    def isDone(self):
        return self.__checkForStates(_PQS.ALL_REWARDS_GOTTEN)

    def needToGetMainReward(self):
        return self.__checkForStates(_PQS.NEED_GET_ALL_REWARDS, _PQS.NEED_GET_MAIN_REWARD)

    def needToGetAddReward(self):
        return self.__checkForStates(_PQS.NEED_GET_ALL_REWARDS, _PQS.NEED_GET_ADD_REWARD)

    def needToGetAllReward(self):
        return self.__checkForStates(_PQS.NEED_GET_ALL_REWARDS)

    def needToGetReward(self):
        return self.__checkForStates(*_PQS.NEED_GET_REWARD)

    def updateProgress(self, questsProgress):
        self.__pqProgress = questsProgress.getPotapovQuestProgress(self.__pqType, self._id)

    def getBonuses(self, bonusName = None, isMain = None):
        if isMain is None:
            data = (self.__pqType.mainQuestInfo, self.__pqType.addQuestInfo)
        elif isMain:
            data = (self.__pqType.mainQuestInfo,)
        else:
            data = (self.__pqType.addQuestInfo,)
        result = []
        for d in data:
            for n, v in d.get('bonus', {}).iteritems():
                if bonusName is not None and n != bonusName:
                    continue
                b = getBonusObj(self, n, v)
                if b is not None:
                    result.append(b)

        return sorted(result, cmp=compareBonuses, key=operator.methodcaller('getName'))

    def getTankmanBonus(self):
        for isMainBonus in (True, False):
            for bonus in self.getBonuses(isMain=isMainBonus):
                if bonus.getName() == 'potapovTankmen':
                    return (bonus, isMainBonus)

        return (None, None)

    def __checkForStates(self, *statesToCheck):
        return self.__pqProgress is not None and self.__pqProgress.state in statesToCheck

    def __repr__(self):
        return 'PQuest<id=%d; state=%s; unlocked=%s>' % (self._id, self.__pqProgress.state, self.isUnlocked())


class MotiveQuest(Quest):

    def getUserName(self):
        return i18n.makeString(Quest.getUserName(self))

    def getGroupID(self):
        return DEFAULTS_GROUPS.MOTIVE_QUESTS

    def getDescription(self):
        return i18n.makeString(Quest.getDescription(self))

    def getParents(self):
        return {}

    def getTips(self):
        return getLocalizedData(self._data, 'advice')

    def getAwardMsg(self):
        return getLocalizedData(self._data, 'congratulation')

    def getRequirementsStr(self):
        return getLocalizedData(self._data, 'requirements')


class FalloutConfig(namedtuple('FalloutConfig', ['allowedVehicles',
 'allowedLevels',
 'additionalTags',
 'minVehiclesPerPlayer',
 'maxVehiclesPerPlayer',
 'vehicleLevelRequired'])):
    itemsCache = dependency.descriptor(IItemsCache)

    def getAllowedVehicles(self):
        result = []
        for v in self.allowedVehicles:
            try:
                item = self.itemsCache.items.getItemByCD(v)
            except KeyError:
                LOG_CURRENT_EXCEPTION()
                item = None

            if item is not None and item.isInInventory:
                result.append(item)

        return sorted(result)

    def hasRequiredVehicles(self):
        allowedVehicles = self.getAllowedVehicles()
        if len(allowedVehicles) < self.minVehiclesPerPlayer:
            return False
        for v in allowedVehicles:
            if v.level == self.vehicleLevelRequired:
                return True

        return False


FalloutConfig.__new__.__defaults__ = ((),
 set(),
 set(),
 0,
 0,
 0)

def _getTileIconPath(tileIconID, prefix, state):
    return '../maps/icons/quests/tiles/%s_%s_%s.png' % (tileIconID, prefix, state)


def getTileNormalUpIconPath(tileIconID):
    return _getTileIconPath(tileIconID, 'color', 'up')


def getTileNormalOverIconPath(tileIconID):
    return _getTileIconPath(tileIconID, 'color', 'over')


def getTileGrayUpIconPath(tileIconID):
    return _getTileIconPath(tileIconID, 'gray', 'up')


def getTileGrayOverIconPath(tileIconID):
    return _getTileIconPath(tileIconID, 'gray', 'over')


def getTileAnimationPath(tileIconID):
    return '../flash/animations/questTiles/%s.swf' % tileIconID


def createQuest(questType, qID, data, progress = None, expiryTime = None):
    if questType == constants.EVENT_TYPE.PERSONAL_QUEST:
        return PersonalQuest(qID, data, progress, expiryTime)
    if questType == constants.EVENT_TYPE.GROUP:
        return Group(qID, data)
    if questType == constants.EVENT_TYPE.MOTIVE_QUEST:
        return MotiveQuest(qID, data, progress)
    if questType == constants.EVENT_TYPE.RANKED_QUEST:
        return RankedQuest(qID, data, progress)
    if questType == constants.EVENT_TYPE.TOKEN_QUEST:
        return TokenQuest(qID, data, progress)
    return Quest(qID, data, progress)


def createAction(eventType, aID, data):
    if eventType == constants.EVENT_TYPE.GROUP:
        return Group(aID, data)
    return Action(aID, data)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\server_events\event_items.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:49:23 St�edn� Evropa (letn� �as)
