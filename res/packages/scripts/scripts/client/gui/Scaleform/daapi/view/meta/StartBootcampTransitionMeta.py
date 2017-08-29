# 2017.08.29 21:48:25 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StartBootcampTransitionMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class StartBootcampTransitionMeta(BaseDAAPIComponent):

    def as_setTransitionTextS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_setTransitionText(text)

    def as_updateStageS(self, width, height):
        if self._isDAAPIInited():
            return self.flashObject.as_updateStage(width, height)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\StartBootcampTransitionMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:25 Støední Evropa (letní èas)
