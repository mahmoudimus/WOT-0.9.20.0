# 2017.08.29 21:48:05 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BCTooltipsWindowMeta.py
from gui.Scaleform.framework.entities.View import View

class BCTooltipsWindowMeta(View):

    def animFinish(self):
        self._printOverrideError('animFinish')

    def as_setRotateTipVisibilityS(self, Visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setRotateTipVisibility(Visible)

    def as_showHandlerS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showHandler()

    def as_completeHandlerS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_completeHandler()

    def as_hideHandlerS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideHandler()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BCTooltipsWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:05 St�edn� Evropa (letn� �as)
