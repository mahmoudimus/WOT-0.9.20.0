# 2017.08.29 21:48:07 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanPersonalInvitesViewMeta.py
from gui.Scaleform.daapi.view.lobby.clans.invites.ClanInvitesViewWithTable import ClanInvitesViewWithTable

class ClanPersonalInvitesViewMeta(ClanInvitesViewWithTable):

    def acceptInvite(self, dbID):
        self._printOverrideError('acceptInvite')

    def declineInvite(self, dbID):
        self._printOverrideError('declineInvite')

    def setInviteSelected(self, dbID, selected):
        self._printOverrideError('setInviteSelected')

    def setSelectAllInvitesCheckBoxSelected(self, selected):
        self._printOverrideError('setSelectAllInvitesCheckBoxSelected')

    def declineAllSelectedInvites(self):
        self._printOverrideError('declineAllSelectedInvites')

    def as_setDeclineAllSelectedInvitesStateS(self, text, enabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setDeclineAllSelectedInvitesState(text, enabled)

    def as_setSelectAllCheckboxStateS(self, selected, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectAllCheckboxState(selected, visible)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\ClanPersonalInvitesViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:07 St�edn� Evropa (letn� �as)
