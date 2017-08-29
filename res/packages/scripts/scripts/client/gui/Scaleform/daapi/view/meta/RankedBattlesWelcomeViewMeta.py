# 2017.08.29 21:48:22 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RankedBattlesWelcomeViewMeta.py
from gui.Scaleform.daapi.view.meta.WrapperViewMeta import WrapperViewMeta

class RankedBattlesWelcomeViewMeta(WrapperViewMeta):

    def onCloseBtnClick(self):
        self._printOverrideError('onCloseBtnClick')

    def onNextBtnClick(self):
        self._printOverrideError('onNextBtnClick')

    def onEscapePress(self):
        self._printOverrideError('onEscapePress')

    def onAnimationFinished(self, forced):
        self._printOverrideError('onAnimationFinished')

    def onSoundTrigger(self, trigerName):
        self._printOverrideError('onSoundTrigger')

    def as_setDataS(self, data):
        """
        :param data: Represented by WelcomeViewVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\RankedBattlesWelcomeViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:22 Støední Evropa (letní èas)
