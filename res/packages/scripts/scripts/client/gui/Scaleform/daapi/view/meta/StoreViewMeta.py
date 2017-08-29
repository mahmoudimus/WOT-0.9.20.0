# 2017.08.29 21:48:26 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StoreViewMeta.py
from gui.Scaleform.framework.entities.View import View

class StoreViewMeta(View):

    def onClose(self):
        self._printOverrideError('onClose')

    def onTabChange(self, tabId):
        self._printOverrideError('onTabChange')

    def onBackButtonClick(self):
        self._printOverrideError('onBackButtonClick')

    def as_showStorePageS(self, tabId):
        if self._isDAAPIInited():
            return self.flashObject.as_showStorePage(tabId)

    def as_initS(self, data):
        """
        :param data: Represented by StoreViewInitVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_init(data)

    def as_showBackButtonS(self, label, description):
        if self._isDAAPIInited():
            return self.flashObject.as_showBackButton(label, description)

    def as_hideBackButtonS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideBackButton()

    def as_setBtnTabCountersS(self, counters):
        """
        :param counters: Represented by Vector.<CountersVo> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setBtnTabCounters(counters)

    def as_removeBtnTabCountersS(self, counters):
        """
        :param counters: Represented by Vector.<String> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_removeBtnTabCounters(counters)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\StoreViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:26 Støední Evropa (letní èas)
