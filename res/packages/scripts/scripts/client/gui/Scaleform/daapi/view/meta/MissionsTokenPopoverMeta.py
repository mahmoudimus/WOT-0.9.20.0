# 2017.08.29 21:48:17 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MissionsTokenPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class MissionsTokenPopoverMeta(SmartPopOverView):

    def onQuestClick(self, idx):
        self._printOverrideError('onQuestClick')

    def onBuyBtnClick(self):
        self._printOverrideError('onBuyBtnClick')

    def as_setStaticDataS(self, data):
        """
        :param data: Represented by MissionsTokenPopoverVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setStaticData(data)

    def as_setListDataProviderS(self, data):
        """
        :param data: Represented by DataProvider.<TokenRendererVO> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setListDataProvider(data)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\MissionsTokenPopoverMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:17 Støední Evropa (letní èas)
