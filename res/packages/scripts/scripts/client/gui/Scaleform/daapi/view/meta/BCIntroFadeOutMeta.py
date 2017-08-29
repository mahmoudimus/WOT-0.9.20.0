# 2017.08.29 21:48:03 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BCIntroFadeOutMeta.py
from gui.Scaleform.framework.entities.View import View

class BCIntroFadeOutMeta(View):

    def finished(self):
        self._printOverrideError('finished')

    def handleError(self, data):
        self._printOverrideError('handleError')

    def as_StartFadeoutS(self, animationTime):
        if self._isDAAPIInited():
            return self.flashObject.as_StartFadeout(animationTime)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BCIntroFadeOutMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:03 Støední Evropa (letní èas)
