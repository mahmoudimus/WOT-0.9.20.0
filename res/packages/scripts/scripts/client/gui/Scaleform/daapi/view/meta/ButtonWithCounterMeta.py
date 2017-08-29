# 2017.08.29 21:48:06 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ButtonWithCounterMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ButtonWithCounterMeta(BaseDAAPIComponent):

    def as_setCountS(self, num):
        if self._isDAAPIInited():
            return self.flashObject.as_setCount(num)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\ButtonWithCounterMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:06 Støední Evropa (letní èas)
