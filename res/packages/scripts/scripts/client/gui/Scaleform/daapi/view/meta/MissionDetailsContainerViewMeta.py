# 2017.08.29 21:48:16 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MissionDetailsContainerViewMeta.py
from gui.Scaleform.framework.entities.View import View

class MissionDetailsContainerViewMeta(View):

    def closeView(self):
        self._printOverrideError('closeView')

    def onChangePage(self, eventID):
        self._printOverrideError('onChangePage')

    def onTokenBuyClick(self, tokenId, questId):
        self._printOverrideError('onTokenBuyClick')

    def as_setInitDataS(self, data):
        """
        :param data: Represented by MissionDetailsContainerVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\MissionDetailsContainerViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:16 Støední Evropa (letní èas)
