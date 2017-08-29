# 2017.08.29 21:48:02 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BCAppearManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BCAppearManagerMeta(BaseDAAPIComponent):

    def onComponentTweenComplete(self, componentId):
        self._printOverrideError('onComponentTweenComplete')

    def onComponentPrepareAppear(self, componentId):
        self._printOverrideError('onComponentPrepareAppear')

    def as_showAnimatedS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showAnimated(data)

    def as_setAppearConfigS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setAppearConfig(data)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BCAppearManagerMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:02 Støední Evropa (letní èas)
