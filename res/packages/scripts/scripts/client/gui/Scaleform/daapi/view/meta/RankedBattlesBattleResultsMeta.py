# 2017.08.29 21:48:21 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RankedBattlesBattleResultsMeta.py
from gui.Scaleform.daapi.view.meta.WrapperViewMeta import WrapperViewMeta

class RankedBattlesBattleResultsMeta(WrapperViewMeta):

    def closeView(self):
        self._printOverrideError('closeView')

    def ready(self):
        self._printOverrideError('ready')

    def as_setDataS(self, data):
        """
        :param data: Represented by RankedBattleResultsVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\RankedBattlesBattleResultsMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:21 St�edn� Evropa (letn� �as)
