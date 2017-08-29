# 2017.08.29 21:48:04 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BCNationsWindowMeta.py
from gui.Scaleform.framework.entities.View import View

class BCNationsWindowMeta(View):

    def onNationSelected(self, nationId):
        self._printOverrideError('onNationSelected')

    def onNationShow(self, nationId):
        self._printOverrideError('onNationShow')

    def as_selectNationS(self, nationId, nationsList):
        """
        :param nationsList: Represented by Vector.<int> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_selectNation(nationId, nationsList)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BCNationsWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:04 Støední Evropa (letní èas)
