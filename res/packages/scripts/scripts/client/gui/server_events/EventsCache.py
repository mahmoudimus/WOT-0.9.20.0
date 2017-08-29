# 2017.08.29 21:49:20 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/server_events/EventsCache.py
import cPickle as pickle
import math
import sys
import zlib
from collections import defaultdict
import BigWorld
import motivation_quests
import nations
from Event import Event, EventManager
from PlayerEvents import g_playerEvents
from adisp import async, process
from constants import EVENT_TYPE, EVENT_CLIENT_DATA, QUEUE_TYPE, ARENA_BONUS_TYPE
from debug_utils import LOG_CURRENT_EXCEPTION, LOG_DEBUG
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK
from gui.server_events import caches as quests_caches
from gui.server_events.PQController import RandomPQController, FalloutPQController
from gui.server_events.event_items import EventBattles, createQuest, createAction, FalloutConfig, MotiveQuest
from gui.server_events.formatters import isMarathon, getLinkedActionID
from gui.server_events.modifiers import ACTION_SECTION_TYPE, ACTION_MODIFIER_TYPE
from gui.server_events.prefetcher import Prefetcher
from gui.shared import events
from gui.shared.gui_items import GUI_ITEM_TYPE, ACTION_ENTITY_ITEM as aei
from gui.shared.utils.RareAchievementsCache import g_rareAchievesCache
from gui.shared.utils.requesters.QuestsProgressRequester import QuestsProgressRequester
from helpers import dependency
from helpers import isPlayerAccount
from items import getTypeOfCompactDescr
from potapov_quests import _POTAPOV_QUEST_XML_PATH
from quest_cache_helpers import readQuestsFromFile
from shared_utils import makeTupleByDict
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache
QUEUE_TYPE_TO_ARENA_BONUS_TYPE = {QUEUE_TYPE.FALLOUT_CLASSIC: ARENA_BONUS_TYPE.FALLOUT_CLASSIC,
 QUEUE_TYPE.FALLOUT_MULTITEAM: ARENA_BONUS_TYPE.FALLOUT_MULTITEAM}

def _defaultQuestMaker(qID, qData, progress):
    return createQuest(qData.get('type', 0), qID, qData, progress.getQuestProgress(qID), progress.getTokenExpiryTime(qData.get('requiredToken')))


def _motiveQuestMaker(qID, qData, progress):
    return MotiveQuest(qID, qData, progress.getQuestProgress(qID))


class _PotapovComposer(object):

    def __init__(self, random, fallout):
        super(_PotapovComposer, self).__init__()
        self.__composedObjects = [random, fallout]

    def getQuests(self):
        return self.__composeDict('getQuests')

    def getTiles(self):
        return self.__composeDict('getTiles')

    def getSelectedQuests(self):
        return self.__composeDict('getSelectedQuests')

    def hasQuestsForReward(self):
        return any((obj.hasQuestsForReward() for obj in self.__composedObjects))

    def hasQuestsForSelect(self):
        return any((obj.hasQuestsForSelect() for obj in self.__composedObjects))

    def getNextTankwomanIDs(self, *args):
        return self.__composedObjects[0].getNextTankwomanIDs(*args)

    def __composeDict(self, getter):
        result = {}
        for obj in self.__composedObjects:
            result.update(getattr(obj, getter)())

        return result


class EventsCache(IEventsCache):
    USER_QUESTS = (EVENT_TYPE.BATTLE_QUEST,
     EVENT_TYPE.TOKEN_QUEST,
     EVENT_TYPE.PERSONAL_QUEST,
     EVENT_TYPE.POTAPOV_QUEST)
    SYSTEM_QUESTS = (EVENT_TYPE.REF_SYSTEM_QUEST,)
    lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self):
        self.__waitForSync = False
        self.__invalidateCbID = None
        self.__cache = defaultdict(dict)
        self.__potapovHidden = {}
        self.__actionsCache = defaultdict(lambda : defaultdict(dict))
        self.__actions2quests = {}
        self.__quests2actions = {}
        self.__questsDossierBonuses = defaultdict(set)
        self.__compensations = {}
        self.__random = RandomPQController()
        self.__fallout = FalloutPQController()
        self.__potapovComposer = _PotapovComposer(self.__random, self.__fallout)
        self.__questsProgress = QuestsProgressRequester()
        self.__em = EventManager()
        self.__prefetcher = Prefetcher(self)
        self.onSyncStarted = Event(self.__em)
        self.onSyncCompleted = Event(self.__em)
        self.onSelectedQuestsChanged = Event(self.__em)
        self.onSlotsCountChanged = Event(self.__em)
        self.onProgressUpdated = Event(self.__em)
        self.onEventsVisited = Event(self.__em)
        self.onProfileVisited = Event(self.__em)
        self.__lockedQuestIds = {}
        return

    def init(self):
        self.__random.init()
        self.__fallout.init()
        self.__prefetcher.init()

    def fini(self):
        self.__fallout.fini()
        self.__random.fini()
        self.__prefetcher.fini()
        self.__em.clear()
        self.__compensations.clear()
        self.__clearInvalidateCallback()

    def start(self):
        self.__lockedQuestIds = BigWorld.player().potapovQuestsLock
        g_playerEvents.onPQLocksChanged += self.__onLockedQuestsChanged

    def stop(self):
        g_playerEvents.onPQLocksChanged -= self.__onLockedQuestsChanged

    def clear(self):
        self.stop()
        quests_caches.clearNavInfo()

    @property
    def waitForSync(self):
        return self.__waitForSync

    @property
    def falloutQuestsProgress(self):
        return self.__fallout.questsProgress

    @property
    def randomQuestsProgress(self):
        return self.__random.questsProgress

    @property
    def random(self):
        return self.__random

    @property
    def fallout(self):
        return self.__fallout

    @property
    def questsProgress(self):
        return self.__questsProgress

    @property
    def potapov(self):
        return self.__potapovComposer

    @property
    def prefetcher(self):
        return self.__prefetcher

    def getLockedQuestTypes(self):
        questIDs = set()
        result = set()
        allQuests = self.potapov.getQuests()
        for lockedList in self.__lockedQuestIds.values():
            if lockedList is not None:
                questIDs.update(lockedList)

        for questID in questIDs:
            if questID in allQuests:
                result.add(allQuests[questID].getMajorTag())

        return result

    @async
    @process
    def update(self, diff = None, callback = None):
        yield self.falloutQuestsProgress.request()
        yield self.randomQuestsProgress.request()
        yield self.__questsProgress.request()
        isNeedToInvalidate = True
        isNeedToClearItemsCaches = False

        def _cbWrapper(*args):
            self.__random.update(self, diff)
            self.__fallout.update(self, diff)
            callback(*args)

        if diff is not None:
            isQPUpdated = 'quests' in diff or 'tokens' in diff
            isEventsDataUpdated = ('eventsData', '_r') in diff or diff.get('eventsData', {})
            isNeedToInvalidate = isQPUpdated or isEventsDataUpdated
            hasVehicleUnlocks = False
            for intCD in diff.get('stats', {}).get('unlocks', set()):
                if getTypeOfCompactDescr(intCD) == GUI_ITEM_TYPE.VEHICLE:
                    hasVehicleUnlocks = True
                    break

            isNeedToClearItemsCaches = 'inventory' in diff and GUI_ITEM_TYPE.VEHICLE in diff['inventory'] or hasVehicleUnlocks
        if isNeedToInvalidate:
            self.__invalidateData(_cbWrapper)
            return
        else:
            if isNeedToClearItemsCaches:
                self.__clearQuestsItemsCache()
            _cbWrapper(True)
            return

    def getQuests(self, filterFunc = None):
        filterFunc = filterFunc or (lambda a: True)

        def userFilterFunc(q):
            return not q.isHidden() and filterFunc(q)

        return self._getQuests(userFilterFunc)

    def getActiveQuests(self, filterFunc = None):
        """ Get active subset of events.
        """
        filterFunc = filterFunc or (lambda a: True)

        def userFilterFunc(q):
            return q.getFinishTimeLeft() and filterFunc(q)

        return self.getQuests(userFilterFunc)

    def getAdvisableQuests(self, filterFunc = None):
        """ Get subset of quests that may be notified as new.
        """
        filterFunc = filterFunc or (lambda a: True)

        def userFilterFunc(q):
            if q.getType() == EVENT_TYPE.MOTIVE_QUEST and not q.isAvailable()[0]:
                return False
            elif q.getType() == EVENT_TYPE.TOKEN_QUEST and isMarathon(q.getID()):
                return False
            else:
                return filterFunc(q)

        return self.getActiveQuests(userFilterFunc)

    def getMotiveQuests(self, filterFunc = None):
        filterFunc = filterFunc or (lambda a: True)

        def userFilterFunc(q):
            return q.getType() == EVENT_TYPE.MOTIVE_QUEST and filterFunc(q)

        return self.getQuests(userFilterFunc)

    def getBattleQuests(self, filterFunc = None):
        filterFunc = filterFunc or (lambda a: True)

        def userFilterFunc(q):
            return q.getType() == EVENT_TYPE.BATTLE_QUEST and filterFunc(q)

        return self.getQuests(userFilterFunc)

    def getGroups(self, filterFunc = None):
        svrGroups = self._getQuestsGroups(filterFunc)
        svrGroups.update(self._getActionsGroups(filterFunc))
        return svrGroups

    def getHiddenQuests(self, filterFunc = None):
        filterFunc = filterFunc or (lambda a: True)

        def hiddenFilterFunc(q):
            return q.isHidden() and filterFunc(q)

        return self._getQuests(hiddenFilterFunc)

    def getRankedQuests(self, filterFunc = None):
        filterFunc = filterFunc or (lambda a: True)

        def rankedFilterFunc(q):
            return q.getType() == EVENT_TYPE.RANKED_QUEST and filterFunc(q)

        return self._getQuests(rankedFilterFunc)

    def getAllQuests(self, filterFunc = None, includePotapovQuests = False):
        return self._getQuests(filterFunc, includePotapovQuests)

    def getActions(self, filterFunc = None):
        filterFunc = filterFunc or (lambda a: True)

        def userFilterFunc(q):
            return filterFunc(q) and q.getType() != EVENT_TYPE.GROUP

        return self._getActions(userFilterFunc)

    def getActionEntities(self):
        return self.__getActionsEntitiesData()

    def getAnnouncedActions(self):
        return self.__getAnnouncedActions()

    def getEventBattles(self):
        battles = self.__getEventBattles()
        if len(battles):
            return EventBattles(battles.get('vehicleTags', set()), battles.get('vehicles', []), bool(battles.get('enabled', 0)), battles.get('arenaTypeID'))
        else:
            return EventBattles(set(), [], 0, None)
            return None

    def isEventEnabled(self):
        return len(self.__getEventBattles()) > 0 and len(self.getEventVehicles()) > 0

    def isGasAttackEnabled(self):
        return len(self.__getGasAttack()) > 0

    @dependency.replace_none_kwargs(itemsCache=IItemsCache)
    def getEventVehicles(self, itemsCache = None):
        result = []
        if itemsCache is None:
            return result
        else:
            for v in self.getEventBattles().vehicles:
                item = itemsCache.items.getItemByCD(v)
                if item.isInInventory:
                    result.append(item)

            return sorted(result)

    def getEvents(self, filterFunc = None):
        svrEvents = self.getQuests(filterFunc)
        svrEvents.update(self.getActions(filterFunc))
        return svrEvents

    def getCurrentEvents(self):
        return self.getEvents(lambda q: q.getStartTimeLeft() <= 0 < q.getFinishTimeLeft())

    def getFutureEvents(self):
        return self.getEvents(lambda q: q.getStartTimeLeft() > 0)

    def isFalloutEnabled(self):
        return bool(self.__getFallout().get('enabled', False))

    def getFalloutConfig(self, queueType):
        arenaBonusType = QUEUE_TYPE_TO_ARENA_BONUS_TYPE.get(queueType, ARENA_BONUS_TYPE.UNKNOWN)
        return makeTupleByDict(FalloutConfig, self.__getFallout().get(arenaBonusType, {}))

    def getAffectedAction(self, item):
        """Get action which affects on given item
        """
        actionEntities = self.getActionEntities()
        if actionEntities:
            entities = actionEntities[aei.ENTITIES_SECTION_NAME]
            actions = actionEntities[aei.ACTIONS_SECTION_NAME]
            steps = actionEntities[aei.STEPS_SECTION_NAME]
            if item in entities:
                entity = entities[item]
                actionNameIdx = entity[aei.ACTION_NAME_IDX]
                actionName = actions[actionNameIdx]
                stepNameIdx = entity[aei.ACTION_STEP_IDX]
                actionStep = steps[stepNameIdx]
                intersectedActions = entity[aei.AFFECTED_ACTIONS_IDX]
                return [actionName, actionStep, intersectedActions]
        return []

    def getItemAction(self, item, isBuying = True, forCredits = False):
        result = []
        type = ACTION_MODIFIER_TYPE.DISCOUNT if isBuying else ACTION_MODIFIER_TYPE.SELLING
        itemTypeID = item.itemTypeID
        nationID = item.nationID
        intCD = item.intCD
        values = self.__actionsCache[ACTION_SECTION_TYPE.ALL][type].get(itemTypeID, {}).get(nationID, [])
        values += self.__actionsCache[ACTION_SECTION_TYPE.ALL][type].get(itemTypeID, {}).get(15, [])
        for (key, value), actionID in values:
            if item.isPremium and key in ('creditsPrice', 'creditsPriceMultiplier') and not forCredits:
                continue
            result.append((value, actionID))

        result.extend(self.__actionsCache[ACTION_SECTION_TYPE.ITEM][type].get(itemTypeID, {}).get(intCD, tuple()))
        return result

    def getBoosterAction(self, booster, isBuying = True, forCredits = False):
        result = []
        type = ACTION_MODIFIER_TYPE.DISCOUNT if isBuying else ACTION_MODIFIER_TYPE.SELLING
        boosterID = booster.boosterID
        values = self.__actionsCache[ACTION_SECTION_TYPE.ALL_BOOSTERS][type].get(nations.NONE_INDEX, [])
        for (key, value), actionID in values:
            if forCredits and key == 'creditsPriceMultiplier':
                result.append((value, actionID))
            elif not forCredits and key == 'goldPriceMultiplier':
                result.append((value, actionID))

        result.extend(self.__actionsCache[ACTION_SECTION_TYPE.BOOSTER][type].get(boosterID, tuple()))
        return result

    def getRentAction(self, item, rentPackage):
        result = []
        type = ACTION_MODIFIER_TYPE.RENT
        itemTypeID = item.itemTypeID
        nationID = item.nationID
        intCD = item.intCD
        values = self.__actionsCache[ACTION_SECTION_TYPE.ALL][type].get(itemTypeID, {}).get(nationID, [])
        values += self.__actionsCache[ACTION_SECTION_TYPE.ALL][type].get(itemTypeID, {}).get(15, [])
        for (key, value), actionID in values:
            result.append((value, actionID))

        result.extend(self.__actionsCache[ACTION_SECTION_TYPE.ITEM][type].get(itemTypeID, {}).get((intCD, rentPackage), tuple()))
        return result

    def getEconomicsAction(self, name):
        result = self.__actionsCache[ACTION_SECTION_TYPE.ECONOMICS][ACTION_MODIFIER_TYPE.DISCOUNT].get(name, [])
        resultMult = self.__actionsCache[ACTION_SECTION_TYPE.ECONOMICS][ACTION_MODIFIER_TYPE.DISCOUNT].get('%sMultiplier' % name, [])
        return tuple(result + resultMult)

    def getCamouflageAction(self, vehicleIntCD):
        return tuple(self.__actionsCache[ACTION_SECTION_TYPE.CUSTOMIZATION][ACTION_MODIFIER_TYPE.DISCOUNT].get(vehicleIntCD, tuple()))

    def getEmblemsAction(self, group):
        return tuple(self.__actionsCache[ACTION_SECTION_TYPE.CUSTOMIZATION][ACTION_MODIFIER_TYPE.DISCOUNT].get(group, tuple()))

    def isBalancedSquadEnabled(self):
        return bool(self.__getUnitRestrictions().get('enabled', False))

    def getBalancedSquadBounds(self):
        return (self.__getUnitRestrictions().get('lowerBound', 0), self.__getUnitRestrictions().get('upperBound', 0))

    def isSquadXpFactorsEnabled(self):
        return bool(self.__getUnitXpFactors().get('enabled', False))

    def getSquadBonusLevelDistance(self):
        return set(self.__getUnitXpFactors().get('levelDistanceWithBonuses', ()))

    def getSquadPenaltyLevelDistance(self):
        return set(self.__getUnitXpFactors().get('levelDistanceWithPenalties', ()))

    def getSquadZeroBonuses(self):
        return set(self.__getUnitXpFactors().get('zeroBonusesFor', ()))

    def getQuestsDossierBonuses(self):
        return self.__questsDossierBonuses

    def getQuestsByTokenRequirement(self, token):
        result = []
        for q in self._getQuests(includePotapovQuests=True).itervalues():
            if token in map(lambda t: t.getID(), q.accountReqs.getTokens()):
                result.append(q)

        return result

    def getQuestsByTokenBonus(self, token):
        result = []
        for q in self._getQuests(includePotapovQuests=True).itervalues():
            for t in q.getBonuses('tokens'):
                if token in t.getTokens().keys():
                    result.append(q)
                    break

        return result

    def getCompensation(self, tokenID):
        """
        Gets bonuses compensation instead of token
        """
        return self.__compensations.get(tokenID)

    def _getQuests(self, filterFunc = None, includePotapovQuests = False):
        result = {}
        groups = {}
        filterFunc = filterFunc or (lambda a: True)
        for qID, q in self.__getCommonQuestsIterator():
            if qID in self.__quests2actions:
                q.linkedActions = self.__quests2actions[qID]
            if q.getType() == EVENT_TYPE.GROUP:
                groups[qID] = q
                continue
            if q.getFinishTimeLeft() <= 0:
                continue
            if not filterFunc(q):
                continue
            result[qID] = q

        if includePotapovQuests:
            for qID, q in self.potapov.getQuests().iteritems():
                if filterFunc(q):
                    result[qID] = q

        for gID, group in groups.iteritems():
            for qID in group.getGroupEvents():
                if qID in result:
                    result[qID].setGroupID(gID)

        children, parents, parentsName = self._makeQuestsRelations(result)
        for qID, q in result.iteritems():
            if qID in children:
                q.setChildren(children[qID])
            if qID in parents:
                q.setParents(parents[qID])
            if qID in parentsName:
                q.setParentsName(parentsName[qID])

        return result

    def _getQuestsGroups(self, filterFunc = None):
        filterFunc = filterFunc or (lambda a: True)
        result = {}
        for qID, q in self.__getCommonQuestsIterator():
            if q.getType() != EVENT_TYPE.GROUP:
                continue
            if not filterFunc(q):
                continue
            result[qID] = q

        return result

    def _getActions(self, filterFunc = None):
        filterFunc = filterFunc or (lambda a: True)
        actions = self.__getActionsData()
        result = {}
        groups = {}
        for aData in actions:
            if 'id' in aData:
                a = self._makeAction(aData['id'], aData)
                actionID = a.getID()
                if actionID in self.__actions2quests:
                    a.linkedQuests = self.__actions2quests[actionID]
                if a.getType() == EVENT_TYPE.GROUP:
                    groups[actionID] = a
                    continue
                if not filterFunc(a):
                    continue
                result[actionID] = a

        for gID, group in groups.iteritems():
            for aID in group.getGroupEvents():
                if aID in result:
                    result[aID].setGroupID(gID)

        return result

    def _getActionsGroups(self, filterFunc = None):
        actions = self.__getActionsData()
        filterFunc = filterFunc or (lambda a: True)
        result = {}
        for aData in actions:
            if 'id' in aData:
                a = self._makeAction(aData['id'], aData)
                if a.getType() != EVENT_TYPE.GROUP:
                    continue
                if not filterFunc(a):
                    continue
                result[a.getID()] = a

        return result

    def _onResync(self, *args):
        self.__invalidateData()

    def _makeQuest(self, qID, qData, maker = _defaultQuestMaker, **kwargs):
        storage = self.__cache['quests']
        if qID in storage:
            return storage[qID]
        q = storage[qID] = maker(qID, qData, self.__questsProgress, **kwargs)
        return q

    def _makeAction(self, aID, aData):
        storage = self.__cache['actions']
        if aID in storage:
            return storage[aID]
        a = storage[aID] = createAction(aData.get('type', 0), aID, aData)
        return a

    @classmethod
    def _makeQuestsRelations(cls, quests):
        makeTokens = defaultdict(list)
        needTokens = defaultdict(list)
        for qID, q in quests.iteritems():
            if q.getType() != EVENT_TYPE.GROUP:
                tokens = q.getBonuses('tokens')
                if len(tokens):
                    for t in tokens[0].getTokens():
                        makeTokens[t].append(qID)

                for t in q.accountReqs.getTokens():
                    needTokens[qID].append(t.getID())

        children = defaultdict(dict)
        for parentID, tokensIDs in needTokens.iteritems():
            for tokenID in tokensIDs:
                children[parentID][tokenID] = makeTokens.get(tokenID, [])

        parents = defaultdict(lambda : defaultdict(list))
        parentsName = defaultdict(lambda : defaultdict(list))
        for parentID, tokens in children.iteritems():
            for tokenID, chn in tokens.iteritems():
                for childID in chn:
                    parents[childID][tokenID].append(parentID)
                    parentsName[childID][tokenID].append(quests[parentID].getUserName())

        return (children, parents, parentsName)

    def __invalidateData(self, callback = lambda *args: None):
        self.__clearCache()
        self.__clearInvalidateCallback()
        self.__waitForSync = True
        self.onSyncStarted()

        def mergeValues(a, b):
            result = list(a)
            result.extend(b)
            return result

        for action in self.getActions().itervalues():
            for modifier in action.getModifiers():
                section = modifier.getSection()
                type = modifier.getType()
                itemType = modifier.getItemType()
                values = modifier.getValues(action)
                currentSection = self.__actionsCache[section][type]
                if itemType is not None:
                    currentSection = currentSection.setdefault(itemType, {})
                for k in values:
                    if k in currentSection:
                        currentSection[k] = mergeValues(currentSection[k], values[k])
                    else:
                        currentSection[k] = values[k]

        rareAchieves = set()
        invalidateTimeLeft = sys.maxint
        for q in self.getCurrentEvents().itervalues():
            dossierBonuses = q.getBonuses('dossier')
            if len(dossierBonuses):
                storage = self.__questsDossierBonuses[q.getID()]
                for bonus in dossierBonuses:
                    records = bonus.getRecords()
                    storage.update(set(bonus.getRecords().keys()))
                    rareAchieves |= set((rId for r, rId in records.iteritems() if r[0] == ACHIEVEMENT_BLOCK.RARE))

            timeLeftInfo = q.getNearestActivityTimeLeft()
            if timeLeftInfo is not None:
                isAvailable, errorMsg = q.isAvailable()
                if not isAvailable:
                    if errorMsg in ('invalid_weekday', 'invalid_time_interval'):
                        invalidateTimeLeft = min(invalidateTimeLeft, timeLeftInfo[0])
                else:
                    intervalBeginTimeLeft, (intervalStart, intervalEnd) = timeLeftInfo
                    invalidateTimeLeft = min(invalidateTimeLeft, intervalBeginTimeLeft + intervalEnd - intervalStart)
            else:
                invalidateTimeLeft = min(invalidateTimeLeft, q.getFinishTimeLeft())

        g_rareAchievesCache.request(rareAchieves)
        for q in self.getFutureEvents().itervalues():
            timeLeftInfo = q.getNearestActivityTimeLeft()
            if timeLeftInfo is None:
                startTime = q.getStartTimeLeft()
            else:
                startTime = timeLeftInfo[0]
            invalidateTimeLeft = min(invalidateTimeLeft, startTime)

        if invalidateTimeLeft != sys.maxint:
            self.__loadInvalidateCallback(invalidateTimeLeft)
        self.__waitForSync = False
        self.__prefetcher.ask()
        self.__syncActionsWithQuests()
        self.__invalidateCompensations()
        self.onSyncCompleted()
        callback(True)
        from gui.shared import g_eventBus
        g_eventBus.handleEvent(events.LobbySimpleEvent(events.LobbySimpleEvent.EVENTS_UPDATED))
        return

    def __invalidateCompensations(self):
        """
        Store hidden quests compensations for marathons quest to improve performance
        """
        self.__compensations.clear()
        for q in self.getHiddenQuests(lambda q: isMarathon(q.getGroupID())).itervalues():
            self.__compensations.update(q.getCompensation())

    def __clearQuestsItemsCache(self):
        for qID, q in self._getQuests().iteritems():
            q.accountReqs.clearItemsCache()
            q.vehicleReqs.clearItemsCache()

    def __syncActionsWithQuests(self):
        """After invalidation of EventsCache, we should sync links between Actions and BattleQuests
        """
        self.__actions2quests.clear()
        self.__quests2actions.clear()
        quests = self.__cache['quests']
        actions = [ item for item in self.__cache['actions'] ]
        self.__actions2quests = {k:[] for k in actions}
        for questID, questData in quests.iteritems():
            groupId = questData.getGroupID()
            linkedActionID = getLinkedActionID(groupId, actions)
            if linkedActionID is not None:
                self.__actions2quests[linkedActionID].append(questID)

        self.__convertQuests2actions()
        return

    def __convertQuests2actions(self):
        """from dict {action: [connected quests]} create reverted dict {quest: [connected actions]}
        :return:
        """
        for action, quests in self.__actions2quests.iteritems():
            for quest in quests:
                if quest in self.__quests2actions:
                    self.__quests2actions[quest].append(action)
                else:
                    self.__quests2actions[quest] = [action]

    @classmethod
    def __getEventsData(cls, eventsTypeName):
        try:
            if isPlayerAccount():
                if eventsTypeName in BigWorld.player().eventsData:
                    return pickle.loads(zlib.decompress(BigWorld.player().eventsData[eventsTypeName]))
                return {}
            LOG_DEBUG('Trying to get quests data from not account player', eventsTypeName, BigWorld.player())
        except Exception:
            LOG_CURRENT_EXCEPTION()

        return {}

    def __getQuestsData(self):
        return self.__getEventsData(EVENT_CLIENT_DATA.QUEST)

    def __getPersonalQuestsData(self):
        return self.__getEventsData(EVENT_CLIENT_DATA.PERSONAL_QUEST)

    def __getActionsData(self):
        return self.__getEventsData(EVENT_CLIENT_DATA.ACTION)

    def __getActionsEntitiesData(self):
        return self.__getEventsData(EVENT_CLIENT_DATA.ACTION_ENTITIES)

    def __getAnnouncedActions(self):
        return self.__getEventsData(EVENT_CLIENT_DATA.ANNOUNCED_ACTION_DATA)

    def __getIngameEventsData(self):
        return self.__getEventsData(EVENT_CLIENT_DATA.INGAME_EVENTS)

    def __getEventBattles(self):
        return self.__getIngameEventsData().get('eventBattles', {})

    def __getUnitRestrictions(self):
        return self.__getUnitData().get('restrictions', {})

    def __getUnitXpFactors(self):
        return self.__getUnitData().get('xpFactors', {})

    def __getFallout(self):
        return self.__getEventsData(EVENT_CLIENT_DATA.FALLOUT)

    def __getUnitData(self):
        return self.__getEventsData(EVENT_CLIENT_DATA.SQUAD_BONUSES)

    def __getGasAttack(self):
        return self.__getEventsData(EVENT_CLIENT_DATA.INGAME_EVENTS).get('gasAttack', {})

    def __getCommonQuestsIterator(self):
        questsData = self.__getQuestsData()
        questsData.update(self.__getPersonalQuestsData())
        questsData.update(self.__getPotapovHiddenQuests())
        for qID, qData in questsData.iteritems():
            yield (qID, self._makeQuest(qID, qData))

        motiveQuests = motivation_quests.g_cache.getAllQuests() or []
        for questDescr in motiveQuests:
            yield (questDescr.questID, self._makeQuest(questDescr.questID, questDescr.questData, maker=_motiveQuestMaker))

    def __loadInvalidateCallback(self, duration):
        LOG_DEBUG('load quest window invalidation callback (secs)', duration)
        self.__clearInvalidateCallback()
        self.__invalidateCbID = BigWorld.callback(math.ceil(duration), self.__invalidateData)

    def __clearInvalidateCallback(self):
        if self.__invalidateCbID is not None:
            BigWorld.cancelCallback(self.__invalidateCbID)
            self.__invalidateCbID = None
        return

    def __clearCache(self):
        self.__questsDossierBonuses.clear()
        self.__actionsCache.clear()
        for storage in self.__cache.itervalues():
            storage.clear()

    def __getPotapovHiddenQuests(self):
        if not self.__potapovHidden:
            xmlPath = _POTAPOV_QUEST_XML_PATH + '/tiles.xml'
            for quest in readQuestsFromFile(xmlPath, EVENT_TYPE.TOKEN_QUEST):
                self.__potapovHidden[quest[0]] = quest[3]

        return self.__potapovHidden.copy()

    def __onLockedQuestsChanged(self):
        self.__lockedQuestIds = BigWorld.player().potapovQuestsLock
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\server_events\EventsCache.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:49:21 St�edn� Evropa (letn� �as)
