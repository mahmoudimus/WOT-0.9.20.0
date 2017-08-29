# 2017.08.29 21:48:05 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BootcampDialogMeta.py
from gui.Scaleform.daapi.view.dialogs.SimpleDialog import SimpleDialog

class BootcampDialogMeta(SimpleDialog):

    def as_setDataS(self, path, label, showAward, awardText):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(path, label, showAward, awardText)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BootcampDialogMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:05 Støední Evropa (letní èas)
