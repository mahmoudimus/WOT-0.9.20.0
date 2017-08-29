# 2017.08.29 21:49:28 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/ClanCache.py
from collections import namedtuple
import BigWorld
from Event import Event
from account_helpers import getAccountDatabaseID
from adisp import async, process
from constants import CLAN_MEMBER_FLAGS
from debug_utils import LOG_ERROR
from helpers import dependency
from helpers import html
from gui.clans.formatters import getClanRoleString
from gui.shared.utils import code2str
from messenger.ext import passCensor
from messenger.storage import storage_getter
from skeletons.gui.shared import IItemsCache

class ClanInfo(namedtuple('ClanInfo', ['clanName',
 'clanAbbrev',
 'chatChannelDBID',
 'memberFlags',
 'enteringTime'])):

    def getClanName(self):
        return self.clanName

    def getClanAbbrev(self):
        return self.clanAbbrev

    def getMembersFlags(self):
        return self.memberFlags

    def getJoiningTime(self):
        return self.enteringTime


class _ClanCache(object):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self):
        self.__waitForSync = False
        self.__strongholdProvider = None
        self.__clanMembersLen = None
        self.__clanMotto = ''
        self.__clanDescription = ''
        self.onSyncStarted = Event()
        self.onSyncCompleted = Event()
        return

    def init(self):
        from gui.shared.stronghold.stronghold_provider import ClientStrongholdProvider
        self.__strongholdProvider = ClientStrongholdProvider()

    def fini(self):
        self.onSyncStarted.clear()
        self.onSyncCompleted.clear()
        self.clear()
        self.__strongholdProvider = None
        return

    def onAccountShowGUI(self):
        self.__startStrongholdProvider()

    def onAvatarBecomePlayer(self):
        self.__stopStrongholdProvider()

    def onDisconnected(self):
        self.__stopStrongholdProvider()

    @property
    def waitForSync(self):
        return self.__waitForSync

    @async
    def update(self, diff = None, callback = None):
        self.__invalidateData(diff, callback)

    def clear(self):
        if self.__strongholdProvider is not None:
            self.__strongholdProvider.stop()
        return

    @storage_getter('users')
    def usersStorage(self):
        return None

    @property
    def clanDBID(self):
        return self.itemsCache.items.stats.clanDBID

    @property
    def isInClan(self):
        """
        @return: is current player in clan
        """
        return self.clanDBID is not None and self.clanDBID != 0

    @property
    def clanMembers(self):
        members = set()
        if self.isInClan:
            members = set(self.usersStorage.getClanMembersIterator(False))
        return members

    @property
    def clanInfo(self):
        info = self.itemsCache.items.stats.clanInfo
        if info and len(info) > 1:
            return info
        else:
            return (None, None, -1, 0, 0)

    @property
    def clanName(self):
        return passCensor(html.escape(self.clanInfo[0]))

    @property
    def clanAbbrev(self):
        return self.clanInfo[1]

    @property
    def clanMotto(self):
        return self.__clanMotto

    @property
    def clanDescription(self):
        return self.__clanDescription

    @property
    def clanTag(self):
        result = self.clanAbbrev
        if result:
            return '[%s]' % result
        return result

    @property
    def clanCommanderName(self):
        for member in self.clanMembers:
            if member.getClanRole() == CLAN_MEMBER_FLAGS.LEADER:
                return member.getName()

        return None

    @property
    def clanRole(self):
        user = self.usersStorage.getUser(getAccountDatabaseID())
        if user:
            role = user.getClanRole()
        else:
            role = 0
        return role

    @property
    def isClanLeader(self):
        return self.clanRole == CLAN_MEMBER_FLAGS.LEADER

    @async
    @process
    def getClanEmblemID(self, callback):
        clanEmblem = None
        if self.isInClan:
            tID = 'clanInfo' + BigWorld.player().name
            clanEmblem = yield self.getClanEmblemTextureID(self.clanDBID, False, tID)
        callback(clanEmblem)
        return

    @async
    def getFileFromServer(self, clanId, fileType, callback):
        if not BigWorld.player().serverSettings['file_server'].has_key(fileType):
            LOG_ERROR("Invalid server's file type: %s" % fileType)
            self._valueResponse(0, (None, None), callback)
            return None
        else:
            clan_emblems = BigWorld.player().serverSettings['file_server'][fileType]
            BigWorld.player().customFilesCache.get(clan_emblems['url_template'] % clanId, lambda url, file: self._valueResponse(0, (url, file), callback), True)
            return None

    @async
    @process
    def getClanEmblemTextureID(self, clanDBID, isBig, textureID, callback):
        import imghdr
        if clanDBID is not None and clanDBID != 0:
            _, clanEmblemFile = yield self.getFileFromServer(clanDBID, 'clan_emblems_small' if not isBig else 'clan_emblems_big')
            if clanEmblemFile and imghdr.what(None, clanEmblemFile) is not None:
                BigWorld.wg_addTempScaleformTexture(textureID, clanEmblemFile)
                callback(textureID)
                return
        callback(None)
        return

    def getClanRoleUserString(self):
        position = self.clanInfo[3]
        return getClanRoleString(position)

    def onClanInfoReceived(self, clanDBID, clanName, clanAbbrev, clanMotto, clanDescription):
        self.__clanMotto = passCensor(html.escape(clanMotto))
        self.__clanDescription = passCensor(html.escape(clanDescription))

    def _valueResponse(self, resID, value, callback):
        if resID < 0:
            LOG_ERROR('[class %s] There is error while getting data from cache: %s[%d]' % (self.__class__.__name__, code2str(resID), resID))
            return callback(value)
        callback(value)

    def _onResync(self):
        if not self.__waitForSync:
            self.__invalidateData()

    def __invalidateData(self, diff = None, callback = lambda *args: None):
        callback(True)

    def __startStrongholdProvider(self):
        self.__strongholdProvider.start()

    def __stopStrongholdProvider(self):
        self.__strongholdProvider.stop()

    def __me_onClanMembersListChanged(self):
        clanMembersLen = len(self.clanMembers)
        if self.__clanMembersLen is not None and clanMembersLen != self.__clanMembersLen:
            self.__clanMembersLen = clanMembersLen
        return


g_clanCache = _ClanCache()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\ClanCache.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:49:28 St�edn� Evropa (letn� �as)
