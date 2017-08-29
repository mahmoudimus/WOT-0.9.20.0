# 2017.08.29 21:48:21 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RankedBattlesCyclesViewMeta.py
from gui.Scaleform.daapi.view.meta.WrapperViewMeta import WrapperViewMeta

class RankedBattlesCyclesViewMeta(WrapperViewMeta):

    def onCloseBtnClick(self):
        self._printOverrideError('onCloseBtnClick')

    def onEscapePress(self):
        self._printOverrideError('onEscapePress')

    def onTabClick(self, tabID):
        self._printOverrideError('onTabClick')

    def onLadderBtnClick(self):
        self._printOverrideError('onLadderBtnClick')

    def as_setDataS(self, data):
        """
        :param data: Represented by RankedBattlesCyclesViewVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_updateTabContentS(self, data):
        """
        :param data: Represented by RankedBattlesCyclesViewVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateTabContent(data)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\RankedBattlesCyclesViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:21 Støední Evropa (letní èas)
