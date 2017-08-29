# 2017.08.29 21:49:19 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/server_events/caches.py
from collections import namedtuple
from debug_utils import LOG_ERROR
from helpers import dependency
from shared_utils import first
from gui import nationCompareByIndex, getNationIndex
from gui.shared.utils.decorators import ReprInjector
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER_INDICES, compareByVehTableTypeName
from gui.Scaleform.genConsts.QUESTS_ALIASES import QUESTS_ALIASES as _QA
from skeletons.gui.lobby_context import ILobbyContext
_g_sortedVehs = {}
VehiclesListProps = namedtuple('VehiclesListProps', ['disableChecker',
 'nationIdx',
 'vehTypeIdx',
 'levelIdx',
 'selectedBtn',
 'sortDirect',
 'checkbox'])

def getVehiclesData(listID):
    return _g_sortedVehs.get(listID)


def addVehiclesData(listID, vehs, disableChecker = None, nationIdx = -1, vehTypeIdx = -1, levelIdx = -1, selectedBtn = None, sortDirect = None, checkbox = None):
    listID = str(listID)
    if listID in _g_sortedVehs:
        _, props = _g_sortedVehs[listID]
    else:
        props = VehiclesListProps(disableChecker, nationIdx, vehTypeIdx, levelIdx, selectedBtn, sortDirect, checkbox)
    _g_sortedVehs[listID] = (vehs, props)
    return props


def updateVehiclesDataProps(listID, **kwargs):
    if listID in _g_sortedVehs:
        vehs, props = _g_sortedVehs[listID]
        _g_sortedVehs[listID] = (vehs, props._replace(**kwargs))


def clearVehiclesData():
    _g_sortedVehs.clear()


PQ_TABS = (_QA.SEASON_VIEW_TAB_RANDOM, _QA.SEASON_VIEW_TAB_FALLOUT)

@dependency.replace_none_kwargs(lobbyContext=ILobbyContext)
def getEnabledPQTabs(lobbyContext = None):
    if lobbyContext is not None:
        tabs = list(PQ_TABS)
        if not lobbyContext.getServerSettings().isRegularQuestEnabled():
            tabs.remove(_QA.SEASON_VIEW_TAB_RANDOM)
        if not lobbyContext.getServerSettings().isFalloutQuestEnabled():
            tabs.remove(_QA.SEASON_VIEW_TAB_FALLOUT)
    else:
        tabs = []
    return tabs


class QuestInfo(object):
    __slots__ = ('questID',)

    def __init__(self, *args):
        super(QuestInfo, self).__init__()
        raise len(args) == len(self.__slots__) or AssertionError
        for idx, fieldName in enumerate(self.__slots__):
            object.__setattr__(self, fieldName, args[idx])

    def __setattr__(self, key, value):
        raise AssertionError

    def update(self, **kwargs):
        for key, value in kwargs.iteritems():
            if key in self.__slots__:
                object.__setattr__(self, key, value)
            else:
                LOG_ERROR('Unsupported argument for object:', self, key, value)

        return self

    def clear(self):
        for field_name in self.__slots__:
            object.__setattr__(self, field_name, None)

        return


class PQInfo(QuestInfo):
    __slots__ = ('tileID', 'questID', 'filters')


@ReprInjector.simple('tabID', 'random', 'falloutQuests')

class _NavigationInfo(object):

    def __init__(self):
        self.tabID = None
        self.random = PQInfo(None, None, None)
        self.falloutQuests = PQInfo(None, None, None)
        self.__selectedPQType = _QA.SEASON_VIEW_TAB_RANDOM
        self._missionsTab = None
        self._vehicleSelectorFilters = {}
        return

    @property
    def selectedPQ(self):
        if self.selectedPQType == _QA.SEASON_VIEW_TAB_RANDOM:
            return self.random
        else:
            return self.falloutQuests

    @property
    def selectedPQType(self):
        if self.__selectedPQType not in getEnabledPQTabs():
            self.__selectedPQType = first(getEnabledPQTabs(), None)
        return self.__selectedPQType

    def setPQTypeByTabID(self, tabID):
        if tabID in PQ_TABS:
            self.__selectedPQType = tabID
        else:
            LOG_ERROR('Wrong tabID to set as selected PQ type')

    def selectTab(self, tabID, doResetNavInfo = False):
        if doResetNavInfo:
            if tabID == _QA.TAB_PERSONAL_QUESTS:
                self.random.clear()
                self.falloutQuests.clear()
        self.tabID = tabID

    def selectPotapovQuest(self, tileID, questID = None):
        self.tabID = _QA.TAB_PERSONAL_QUESTS
        self.selectedPQ.update(tileID=tileID, questID=questID)

    def selectRandomQuest(self, tileID, questID = None):
        self.tabID = _QA.TAB_PERSONAL_QUESTS
        self.__selectedPQType = _QA.SEASON_VIEW_TAB_RANDOM
        self.random = self.random.update(tileID=tileID, questID=questID, filters=None)
        return

    def selectFalloutQuest(self, tileID, questID = None):
        self.tabID = _QA.TAB_PERSONAL_QUESTS
        self.__selectedPQType = _QA.SEASON_VIEW_TAB_FALLOUT
        self.falloutQuests = self.falloutQuests.update(tileID=tileID, questID=questID)

    def changePQFilters(self, *args):
        self.selectedPQ.update(filters=args)

    def getMissionsTab(self):
        """ Get current missions tab for the current game session.
        """
        return self._missionsTab

    def setMissionsTab(self, tabID):
        """ Set current missions tab for the current game session.
        """
        self._missionsTab = tabID

    def getVehicleSelectorFilters(self):
        """ Get missions vehicle selector carousel's filters.
        """
        return self._vehicleSelectorFilters

    def setVehicleSelectorFilters(self, filters):
        """ Set missions vehicle selector carousel's filters.
        """
        self._vehicleSelectorFilters = filters


_g_navInfo = None

def getNavInfo():
    global _g_navInfo
    if _g_navInfo is None:
        _g_navInfo = _NavigationInfo()
    return _g_navInfo


def clearNavInfo():
    global _g_navInfo
    _g_navInfo = None
    return
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\server_events\caches.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:49:19 St�edn� Evropa (letn� �as)
