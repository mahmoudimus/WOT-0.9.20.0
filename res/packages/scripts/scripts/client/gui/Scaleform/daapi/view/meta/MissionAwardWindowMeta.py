# 2017.08.29 21:48:16 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MissionAwardWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class MissionAwardWindowMeta(AbstractWindowView):

    def onCurrentQuestClick(self):
        self._printOverrideError('onCurrentQuestClick')

    def onNextQuestClick(self):
        self._printOverrideError('onNextQuestClick')

    def as_setDataS(self, data):
        """
        :param data: Represented by MissionAwardWindowVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\MissionAwardWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:16 St�edn� Evropa (letn� �as)
