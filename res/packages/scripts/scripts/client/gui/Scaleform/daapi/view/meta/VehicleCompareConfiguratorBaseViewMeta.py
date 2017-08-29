# 2017.08.29 21:48:28 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleCompareConfiguratorBaseViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class VehicleCompareConfiguratorBaseViewMeta(BaseDAAPIComponent):

    def applyConfig(self):
        self._printOverrideError('applyConfig')

    def resetConfig(self):
        self._printOverrideError('resetConfig')

    def onCloseView(self):
        self._printOverrideError('onCloseView')

    def as_setResetEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setResetEnabled(value)

    def as_setApplyEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setApplyEnabled(value)

    def as_setInitDataS(self, data):
        """
        :param data: Represented by VehicleCompareConfiguratorInitDataVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\VehicleCompareConfiguratorBaseViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:28 Støední Evropa (letní èas)
