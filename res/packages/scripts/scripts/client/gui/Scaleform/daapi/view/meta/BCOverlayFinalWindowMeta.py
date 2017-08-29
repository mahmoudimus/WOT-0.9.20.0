# 2017.08.29 21:48:04 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BCOverlayFinalWindowMeta.py
from gui.Scaleform.framework.entities.View import View

class BCOverlayFinalWindowMeta(View):

    def animFinish(self):
        self._printOverrideError('animFinish')

    def as_msgTypeHandlerS(self, msgType, status):
        if self._isDAAPIInited():
            return self.flashObject.as_msgTypeHandler(msgType, status)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BCOverlayFinalWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:04 Støední Evropa (letní èas)
