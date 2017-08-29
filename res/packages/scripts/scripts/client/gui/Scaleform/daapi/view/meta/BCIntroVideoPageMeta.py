# 2017.08.29 21:48:03 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BCIntroVideoPageMeta.py
from gui.Scaleform.framework.entities.View import View

class BCIntroVideoPageMeta(View):

    def videoFinished(self):
        self._printOverrideError('videoFinished')

    def goNext(self):
        self._printOverrideError('goNext')

    def handleError(self, data):
        self._printOverrideError('handleError')

    def as_playVideoS(self, data):
        """
        :param data: Represented by BCIntroVideoVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_playVideo(data)

    def as_updateProgressS(self, percent):
        if self._isDAAPIInited():
            return self.flashObject.as_updateProgress(percent)

    def as_loadedS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_loaded()

    def as_showIntroPageS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showIntroPage(value)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BCIntroVideoPageMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:03 Støední Evropa (letní èas)
