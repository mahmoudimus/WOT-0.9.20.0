# 2017.08.29 21:48:07 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanProfileGlobalMapPromoViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ClanProfileGlobalMapPromoViewMeta(BaseDAAPIComponent):

    def showInfo(self):
        self._printOverrideError('showInfo')

    def showMap(self):
        self._printOverrideError('showMap')

    def as_setDataS(self, data):
        """
        :param data: Represented by ClanProfileGlobalMapPromoVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\ClanProfileGlobalMapPromoViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:07 St�edn� Evropa (letn� �as)
