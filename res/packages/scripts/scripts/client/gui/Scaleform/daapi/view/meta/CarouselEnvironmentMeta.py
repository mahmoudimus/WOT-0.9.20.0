# 2017.08.29 21:48:06 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CarouselEnvironmentMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class CarouselEnvironmentMeta(BaseDAAPIComponent):

    def selectVehicle(self, id):
        self._printOverrideError('selectVehicle')

    def resetFilters(self):
        self._printOverrideError('resetFilters')

    def as_getDataProviderS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDataProvider()

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_setEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setEnabled(value)

    def as_showCounterS(self, countText, isAttention):
        if self._isDAAPIInited():
            return self.flashObject.as_showCounter(countText, isAttention)

    def as_hideCounterS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideCounter()

    def as_blinkCounterS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_blinkCounter()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\CarouselEnvironmentMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:06 Støední Evropa (letní èas)
