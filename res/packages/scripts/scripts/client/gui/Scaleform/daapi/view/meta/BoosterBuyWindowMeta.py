# 2017.08.29 21:48:05 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BoosterBuyWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class BoosterBuyWindowMeta(AbstractWindowView):

    def buy(self, count):
        self._printOverrideError('buy')

    def setAutoRearm(self, autoRearm):
        self._printOverrideError('setAutoRearm')

    def as_setInitDataS(self, data):
        """
        :param data: Represented by BoosterBuyWindowVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_updateDataS(self, data):
        """
        :param data: Represented by BoosterBuyWindowUpdateVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateData(data)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BoosterBuyWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:05 Støední Evropa (letní èas)
