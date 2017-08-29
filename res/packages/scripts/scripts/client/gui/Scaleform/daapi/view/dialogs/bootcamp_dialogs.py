# 2017.08.29 21:46:27 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/bootcamp_dialogs.py
from gui.Scaleform.daapi.view.meta.BootcampDialogMeta import BootcampDialogMeta

class ExecutionChooserDialog(BootcampDialogMeta):

    def __init__(self, meta, handler):
        super(ExecutionChooserDialog, self).__init__(meta.getMessage(), meta.getTitle(), meta.getButtonLabels(), meta.getCallbackWrapper(handler))
        self.__imagePath = meta.getImagePath()
        self.__label = meta.getLabel()
        self.__showAwardIcon = meta.getShowAwardIcon()
        self.__awardingText = meta.getAwardingText()

    def _populate(self):
        super(ExecutionChooserDialog, self)._populate()
        self.as_setDataS(self.__imagePath, self.__label, self.__showAwardIcon, self.__awardingText)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\dialogs\bootcamp_dialogs.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:46:27 Støední Evropa (letní èas)
