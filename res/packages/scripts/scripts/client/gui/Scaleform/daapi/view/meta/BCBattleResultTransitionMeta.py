# 2017.08.29 21:48:03 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BCBattleResultTransitionMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BCBattleResultTransitionMeta(BaseDAAPIComponent):

    def as_msgTypeHandlerS(self, status):
        if self._isDAAPIInited():
            return self.flashObject.as_msgTypeHandler(status)

    def as_updateStageS(self, width, height):
        if self._isDAAPIInited():
            return self.flashObject.as_updateStage(width, height)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BCBattleResultTransitionMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:03 Støední Evropa (letní èas)
