# 2017.08.29 21:48:25 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StatsBaseMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class StatsBaseMeta(BaseDAAPIComponent):

    def acceptSquad(self, uid):
        self._printOverrideError('acceptSquad')

    def addToSquad(self, uid):
        self._printOverrideError('addToSquad')

    def as_setIsIntaractiveS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setIsIntaractive(value)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\StatsBaseMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:25 Støední Evropa (letní èas)
