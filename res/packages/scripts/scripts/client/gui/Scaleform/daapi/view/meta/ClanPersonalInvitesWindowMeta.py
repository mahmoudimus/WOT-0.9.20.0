# 2017.08.29 21:48:07 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanPersonalInvitesWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ClanPersonalInvitesWindowMeta(AbstractWindowView):

    def as_setActualInvitesTextS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setActualInvitesText(value)

    def as_showWaitingAnimationS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showWaitingAnimation(value)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\ClanPersonalInvitesWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:07 St�edn� Evropa (letn� �as)
