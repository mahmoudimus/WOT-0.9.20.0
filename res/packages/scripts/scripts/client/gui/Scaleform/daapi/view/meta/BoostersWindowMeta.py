# 2017.08.29 21:48:05 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BoostersWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class BoostersWindowMeta(AbstractWindowView):

    def requestBoostersArray(self, tabIndex):
        self._printOverrideError('requestBoostersArray')

    def onBoosterActionBtnClick(self, boosterID, questID):
        self._printOverrideError('onBoosterActionBtnClick')

    def onFiltersChange(self, filters):
        self._printOverrideError('onFiltersChange')

    def onResetFilters(self):
        self._printOverrideError('onResetFilters')

    def as_setDataS(self, data):
        """
        :param data: Represented by BoostersWindowVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setStaticDataS(self, data):
        """
        :param data: Represented by BoostersWindowStaticVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setStaticData(data)

    def as_setListDataS(self, boosters, scrollToTop):
        """
        :param boosters: Represented by DataProvider.<BoostersTableRendererVO> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setListData(boosters, scrollToTop)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BoostersWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:05 Støední Evropa (letní èas)
