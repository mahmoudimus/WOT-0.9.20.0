# 2017.08.29 21:47:30 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/rankedBattles/ranked_servers_data_provider.py
import time
import BigWorld
from gui.Scaleform.daapi.view.servers_data_provider import ServersDataProvider
from gui.Scaleform.locale.COMMON import COMMON
from gui.Scaleform.locale.RANKED_BATTLES import RANKED_BATTLES
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from helpers import i18n, dependency
from skeletons.gui.game_control import IRankedBattlesController

class RankedServersDataProvider(ServersDataProvider):
    """
    data provider for ranked servers displaying in ranked battles prime time view
    """
    rankedController = dependency.descriptor(IRankedBattlesController)

    def __init__(self):
        super(RankedServersDataProvider, self).__init__()
        self.primeTimes = self.rankedController.getPrimeTimesForDay(time.time(), groupIdentical=False)
        self.__maxPeriodLen = self.__getMaxPrimeTimes()

    def getDefaultSelectedServer(self, serversList):
        periodStartMin = None
        chosenServer = None
        getByPing = False
        for server in serversList:
            serverPeriods = self.primeTimes[server['shortname']]
            for periodStart, _ in serverPeriods:
                if periodStartMin is None:
                    chosenServer = server['shortname']
                    periodStartMin = periodStart
                elif periodStart < periodStartMin:
                    chosenServer = server['shortname']
                    periodStartMin = periodStart
                elif periodStart == periodStartMin:
                    chosenServer = None
                    getByPing = True

        if not getByPing or not serversList:
            return chosenServer
        elif getByPing:
            minPingServer = serversList[0]
            for server in serversList:
                if server['pingValue'] < minPingServer['pingValue']:
                    minPingServer = server

            return minPingServer['shortname']
        else:
            return

    def setSelectedID(self, sid):
        """
        updates selected status for server
        :param sid: server id
        :return: None
        """
        super(RankedServersDataProvider, self).setSelectedID(sid)
        for vo in self.sortedCollection:
            if vo['id'] == sid:
                vo['selected'] = not vo['selected']
            else:
                vo['selected'] = False

    def _makeVO(self, index, item):
        vo = super(RankedServersDataProvider, self)._makeVO(index, item)
        serverName = item.get('shortname')
        serverPeriods = []
        for scheduleServerNames in self.primeTimes.keys():
            if serverName in scheduleServerNames:
                serverPeriods = self.primeTimes[scheduleServerNames]

        periodsStr = []
        frmt = BigWorld.wg_getShortTimeFormat
        if serverPeriods:
            for periodStart, periodEnd in serverPeriods:
                periodsStr.append(i18n.makeString(RANKED_BATTLES.CALENDARDAY_TIME, start=frmt(periodStart), end=frmt(periodEnd)))

        else:
            periodsStr = i18n.makeString(COMMON.COMMON_DASH)
        vo['tooltip'] = i18n.makeString(TOOLTIPS.RANKED_SERVERNAME, name=serverName)
        vo['shortname'] = item['shortname']
        vo['schedules'] = '\n'.join(periodsStr)
        vo['selected'] = False
        vo['maxPrimeTimes'] = self.__maxPeriodLen
        return vo

    def __getMaxPrimeTimes(self):
        newPrimeTimes = 0
        maxPrimeTimes = 0
        for serverPeriods in self.primeTimes.values():
            newPrimeTimes = len(serverPeriods)
            if maxPrimeTimes < newPrimeTimes:
                maxPrimeTimes = newPrimeTimes

        return maxPrimeTimes
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\rankedBattles\ranked_servers_data_provider.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:47:30 St�edn� Evropa (letn� �as)
