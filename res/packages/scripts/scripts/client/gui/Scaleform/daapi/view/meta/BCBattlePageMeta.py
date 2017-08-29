# 2017.08.29 21:48:02 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BCBattlePageMeta.py
from gui.Scaleform.daapi.view.battle.classic.page import ClassicPage

class BCBattlePageMeta(ClassicPage):

    def onAnimationsComplete(self):
        self._printOverrideError('onAnimationsComplete')

    def as_showAnimatedS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showAnimated(data)

    def as_setAppearConfigS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setAppearConfig(data)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BCBattlePageMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:02 Støední Evropa (letní èas)
