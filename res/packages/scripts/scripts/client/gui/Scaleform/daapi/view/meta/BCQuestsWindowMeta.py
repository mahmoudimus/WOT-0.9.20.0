# 2017.08.29 21:48:04 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BCQuestsWindowMeta.py
from gui.Scaleform.framework.entities.View import View

class BCQuestsWindowMeta(View):

    def onCloseClicked(self):
        self._printOverrideError('onCloseClicked')

    def as_setDataS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(value)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BCQuestsWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:04 Støední Evropa (letní èas)
