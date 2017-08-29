# 2017.08.29 21:48:04 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BCQueueWindowMeta.py
from gui.Scaleform.framework.entities.View import View

class BCQueueWindowMeta(View):

    def cancel(self):
        self._printOverrideError('cancel')

    def as_setDataS(self, data):
        """
        :param data: Represented by BCQueueVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_showCancelButtonS(self, value, label, info):
        if self._isDAAPIInited():
            return self.flashObject.as_showCancelButton(value, label, info)

    def as_setStatusTextS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setStatusText(value)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BCQueueWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:05 Støední Evropa (letní èas)
