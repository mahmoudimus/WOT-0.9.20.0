# 2017.08.29 21:48:11 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ExchangeFreeToTankmanXpWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ExchangeFreeToTankmanXpWindowMeta(AbstractWindowView):

    def apply(self):
        self._printOverrideError('apply')

    def onValueChanged(self, data):
        self._printOverrideError('onValueChanged')

    def calcValueRequest(self, value):
        self._printOverrideError('calcValueRequest')

    def as_setInitDataS(self, value):
        """
        :param value: Represented by ExchangeFreeToTankmanInitVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(value)

    def as_setCalcValueResponseS(self, price, actionPriceData):
        """
        :param actionPriceData: Represented by ActionPriceVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCalcValueResponse(price, actionPriceData)

    def as_setWalletStatusS(self, walletStatus):
        if self._isDAAPIInited():
            return self.flashObject.as_setWalletStatus(walletStatus)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\ExchangeFreeToTankmanXpWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:11 Støední Evropa (letní èas)
