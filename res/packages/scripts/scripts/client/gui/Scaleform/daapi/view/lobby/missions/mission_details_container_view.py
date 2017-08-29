# 2017.08.29 21:47:12 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/missions/mission_details_container_view.py
from async import async, await
from gui.Scaleform.daapi import LobbySubView
from gui.Scaleform.daapi.view.lobby.missions import missions_helper
from gui.Scaleform.daapi.view.lobby.missions.group_packers import getGroupPackerByContextID
from gui.Scaleform.daapi.view.meta.MissionDetailsContainerViewMeta import MissionDetailsContainerViewMeta
from gui.Scaleform.genConsts.QUESTS_ALIASES import QUESTS_ALIASES
from gui.server_events.formatters import parseComplexToken
from gui.shared import events, event_bus_handlers, EVENT_BUS_SCOPE
from helpers import dependency
from skeletons.gui.server_events import IEventsCache

class MissionDetailsContainerView(LobbySubView, MissionDetailsContainerViewMeta):
    eventsCache = dependency.descriptor(IEventsCache)
    __metaclass__ = event_bus_handlers.EventBusListener

    def __init__(self, ctx = None):
        super(MissionDetailsContainerView, self).__init__(ctx)
        self.__ctx = ctx
        self.__groupPacker = None
        self.__quests = {}
        return

    def closeView(self):
        self.destroy()

    def onTokenBuyClick(self, tokenId, questId):
        self.fireEvent(events.OpenLinkEvent(events.OpenLinkEvent.TOKEN_SHOP, params={'name': parseComplexToken(tokenId).webID}))

    def onChangePage(self, eventID):
        vehicleSelector = self.components.get(QUESTS_ALIASES.MISSIONS_VEHICLE_SELECTOR_ALIAS)
        quest = self.__quests.get(eventID)
        criteria, extraConditions = missions_helper.getDetailedMissionData(quest).getVehicleRequirementsCriteria()
        vehicleSelector.as_closeS()
        if criteria and not quest.isCompleted():
            vehicleSelector.setCriteria(criteria, extraConditions)
        else:
            vehicleSelector.as_hideSelectedVehicleS()

    def _populate(self):
        super(MissionDetailsContainerView, self)._populate()
        self.eventsCache.onSyncCompleted += self.__update
        self.__update(needDemand=True)

    def _invalidate(self, ctx = None):
        self.__ctx = ctx
        self.__update(needDemand=False)

    def _dispose(self):
        self.eventsCache.onSyncCompleted -= self.__update
        self.__quests = None
        if self.__groupPacker is not None:
            self.__groupPacker.clear()
            self.__groupPacker = None
        super(MissionDetailsContainerView, self)._dispose()
        return

    @async
    def __update(self, needDemand = True):
        if needDemand:
            yield await(self.eventsCache.prefetcher.demand())
        self.__quests = self.eventsCache.getQuests(lambda q: q.getFinishTimeLeft())
        eventID = self.__ctx.get('eventID')
        groupID = self.__ctx.get('groupID')
        if self.__groupPacker is not None:
            self.__groupPacker.clear()
        self.__groupPacker = getGroupPackerByContextID(groupID, self.eventsCache)
        datailedList = []
        if self.__groupPacker is not None:
            title = self.__groupPacker.getTitle()
            for q in self.__groupPacker.findEvents(self.__quests):
                data = missions_helper.getDetailedMissionData(q).getInfo()
                datailedList.append(data)

        else:
            title = ''
            quest = self.__quests.get(eventID)
            if quest is not None:
                datailedList.append(missions_helper.getDetailedMissionData(quest).getInfo())
        if not datailedList:
            self.closeView()
        else:
            pages = map(lambda (i, mission): {'buttonsGroup': 'MissionDetailsPageGroup',
             'pageIndex': i,
             'label': '%i' % (i + 1),
             'tooltip': mission.get('statusTooltipData'),
             'missionId': mission.get('eventID'),
             'status': mission.get('status'),
             'selected': eventID == mission.get('eventID')}, enumerate(datailedList))
            self.as_setInitDataS({'title': title,
             'missions': datailedList,
             'pages': pages})
        return

    @event_bus_handlers.eventBusHandler(events.HideWindowEvent.HIDE_MISSION_DETAILS_VIEW, EVENT_BUS_SCOPE.LOBBY)
    def __handleDetailsClose(self, _):
        """ We may need to close details externally when it already open.
        """
        self.destroy()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\missions\mission_details_container_view.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:47:12 St�edn� Evropa (letn� �as)
