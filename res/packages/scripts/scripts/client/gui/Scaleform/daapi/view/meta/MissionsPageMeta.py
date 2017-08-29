# 2017.08.29 21:48:16 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MissionsPageMeta.py
from gui.Scaleform.framework.entities.View import View

class MissionsPageMeta(View):

    def resetFilters(self):
        self._printOverrideError('resetFilters')

    def onTabSelected(self, alias):
        self._printOverrideError('onTabSelected')

    def onClose(self):
        self._printOverrideError('onClose')

    def as_setTabsDataProviderS(self, dataProvider):
        """
        :param dataProvider: Represented by DataProvider.<MissionTabVO> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTabsDataProvider(dataProvider)

    def as_showFilterCounterS(self, countText, isFilterApplied):
        if self._isDAAPIInited():
            return self.flashObject.as_showFilterCounter(countText, isFilterApplied)

    def as_blinkFilterCounterS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_blinkFilterCounter()

    def as_setTabsCounterDataS(self, data):
        """
        :param data: Represented by Vector.<MissionTabCounterVO> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTabsCounterData(data)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\MissionsPageMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:17 Støední Evropa (letní èas)
