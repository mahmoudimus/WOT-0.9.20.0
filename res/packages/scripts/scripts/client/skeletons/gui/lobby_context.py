# 2017.08.29 21:51:38 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/skeletons/gui/lobby_context.py


class ILobbyContext(object):

    def clear(self):
        raise NotImplementedError

    def onAccountBecomePlayer(self):
        raise NotImplementedError

    def onAccountShowGUI(self, ctx):
        raise NotImplementedError

    def getArenaUniqueIDByClientID(self, clientArenaID):
        raise NotImplementedError

    def getClientIDByArenaUniqueID(self, arenaUniqueID):
        raise NotImplementedError

    def setCredentials(self, login, token):
        raise NotImplementedError

    def getCredentials(self):
        raise NotImplementedError

    def getBattlesCount(self):
        raise NotImplementedError

    def update(self, diff):
        raise NotImplementedError

    def updateBattlesCount(self, battlesCount):
        raise NotImplementedError

    def updateGuiCtx(self, ctx):
        raise NotImplementedError

    def getGuiCtx(self):
        raise NotImplementedError

    @property
    def collectUiStats(self):
        raise NotImplementedError

    @property
    def needLogUXEvents(self):
        raise NotImplementedError

    def getServerSettings(self):
        raise NotImplementedError

    def setServerSettings(self, serverSettings):
        raise NotImplementedError

    def getPlayerFullName(self, pName, clanInfo = None, clanAbbrev = None, regionCode = None, pDBID = None):
        raise NotImplementedError

    def getClanAbbrev(self, clanInfo):
        raise NotImplementedError

    def getRegionCode(self, dbID):
        raise NotImplementedError

    def isAnotherPeriphery(self, peripheryID):
        raise NotImplementedError

    def isPeripheryAvailable(self, peripheryID, itemsCache = None):
        raise NotImplementedError

    def getPeripheryName(self, peripheryID):
        raise NotImplementedError

    def addHeaderNavigationConfirmator(self, confirmator):
        raise NotImplementedError

    def deleteHeaderNavigationConfirmator(self, confirmator):
        raise NotImplementedError

    def isHeaderNavigationPossible(self, callback = None):
        raise NotImplementedError
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\skeletons\gui\lobby_context.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:51:39 St�edn� Evropa (letn� �as)
