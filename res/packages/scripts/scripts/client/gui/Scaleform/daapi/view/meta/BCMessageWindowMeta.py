# 2017.08.29 21:48:04 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BCMessageWindowMeta.py
from gui.Scaleform.framework.entities.View import View

class BCMessageWindowMeta(View):

    def onMessageRemoved(self):
        self._printOverrideError('onMessageRemoved')

    def onMessageAppear(self, rendrerer):
        self._printOverrideError('onMessageAppear')

    def onMessageDisappear(self, rendrerer):
        self._printOverrideError('onMessageDisappear')

    def onMessageButtonClicked(self):
        self._printOverrideError('onMessageButtonClicked')

    def as_setMessageDataS(self, value):
        """
        :param value: Represented by Array (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setMessageData(value)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BCMessageWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:04 Støední Evropa (letní èas)
