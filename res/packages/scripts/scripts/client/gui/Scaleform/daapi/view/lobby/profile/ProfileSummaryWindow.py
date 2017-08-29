# 2017.08.29 21:47:20 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileSummaryWindow.py
import BigWorld
from adisp import process
from debug_utils import LOG_ERROR
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.shared import event_dispatcher as shared_events
from gui.shared.event_bus import EVENT_BUS_SCOPE
from helpers.i18n import makeString as _ms
from gui.clans.clan_helpers import ClanListener
from gui.clans.formatters import getClanRoleString
from gui.shared.ClanCache import ClanInfo
from gui.shared.formatters import text_styles
from gui.shared.view_helpers.emblems import ClanEmblemsHelper
from gui.Scaleform.daapi.view.meta.ProfileSummaryWindowMeta import ProfileSummaryWindowMeta
from gui.Scaleform.locale.PROFILE import PROFILE
from gui.shared import events

class ProfileSummaryWindow(ProfileSummaryWindowMeta, ClanEmblemsHelper, ClanListener):

    def __init__(self, *args):
        super(ProfileSummaryWindow, self).__init__(*args)
        self.__rating = 0

    def getGlobalRating(self, databaseID):
        if databaseID is not None and not self.__rating:
            self._receiveRating(databaseID)
        return self.__rating

    def openClanStatistic(self):
        if self.lobbyContext.getServerSettings().clanProfile.isEnabled():
            clanID, clanInfo = self.itemsCache.items.getClanInfo(self._userID)
            if clanID != 0:
                clanInfo = ClanInfo(*clanInfo)
                shared_events.showClanProfileWindow(clanID, clanInfo.getClanAbbrev())

    def onClanEmblem32x32Received(self, clanDbID, emblem):
        if emblem:
            path = self.getMemoryTexturePath(emblem)
            self.as_setClanEmblemS(path)

    def onClanStateChanged(self, oldStateID, newStateID):
        self._requestClanInfo()

    def onAccountClanProfileChanged(self, profile):
        self._requestClanInfo()

    def onAccountClanInfoReceived(self, info):
        self._requestClanInfo()

    def _populate(self):
        super(ProfileSummaryWindow, self)._populate()
        self.startClanListening()
        self._requestClanInfo()

    def _dispose(self):
        self.stopClanListening()
        super(ProfileSummaryWindow, self)._dispose()

    def _requestClanInfo(self):
        isShowClanProfileBtnVisible = False
        if self.clansCtrl.isEnabled():
            isShowClanProfileBtnVisible = True
        clanDBID, clanInfo = self.itemsCache.items.getClanInfo(self._userID)
        if clanInfo is not None:
            clanInfo = ClanInfo(*clanInfo)
            clanData = {'id': clanDBID,
             'header': clanInfo.getClanName(),
             'topLabel': _ms(PROFILE.PROFILE_SUMMARY_CLAN_POST),
             'topValue': text_styles.main(getClanRoleString(clanInfo.getMembersFlags())),
             'bottomLabel': _ms(PROFILE.PROFILE_SUMMARY_CLAN_JOINDATE),
             'bottomValue': text_styles.main(BigWorld.wg_getLongDateFormat(clanInfo.getJoiningTime()))}
            btnParams = self._getClanBtnParams(isShowClanProfileBtnVisible)
            clanData.update(btnParams)
            self.as_setClanDataS(clanData)
            self.requestClanEmblem32x32(clanDBID)
        return

    @process
    def _receiveRating(self, databaseID):
        req = self.itemsCache.items.dossiers.getUserDossierRequester(int(databaseID))
        self.__rating = yield req.getGlobalRating()

    def _getClanBtnParams(self, isVisible):
        if self.clansCtrl.isAvailable():
            btnEnabled = True
            btnTooltip = None
        else:
            btnEnabled = False
            btnTooltip = TOOLTIPS.HEADER_ACCOUNTPOPOVER_UNAVAILABLE
        return {'btnLabel': _ms(PROFILE.PROFILE_SUMMARY_CLAN_BTNLABEL),
         'btnEnabled': btnEnabled,
         'btnVisible': isVisible,
         'btnTooltip': btnTooltip}
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\profile\ProfileSummaryWindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:47:20 St�edn� Evropa (letn� �as)
