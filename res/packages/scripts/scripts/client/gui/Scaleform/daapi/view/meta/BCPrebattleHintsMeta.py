# 2017.08.29 21:48:04 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BCPrebattleHintsMeta.py
from gui.Scaleform.framework.entities.View import View

class BCPrebattleHintsMeta(View):

    def as_setHintsVisibilityS(self, visible, hidden):
        """
        :param visible: Represented by Vector.<String> (AS)
        :param hidden: Represented by Vector.<String> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setHintsVisibility(visible, hidden)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BCPrebattleHintsMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:04 Støední Evropa (letní èas)
