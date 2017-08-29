# 2017.08.29 21:52:01 Støední Evropa (letní èas)
# Embedded file name: scripts/client/tutorial/gui/Scaleform/meta/TutorialDialogMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class TutorialDialogMeta(AbstractWindowView):

    def submit(self):
        self._printOverrideError('submit')

    def cancel(self):
        self._printOverrideError('cancel')

    def as_setContentS(self, data):
        """
        :param data: Represented by TutorialDialogVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setContent(data)

    def as_updateContentS(self, data):
        """
        :param data: Represented by TutorialDialogVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateContent(data)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\tutorial\gui\Scaleform\meta\TutorialDialogMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:52:01 Støední Evropa (letní èas)
