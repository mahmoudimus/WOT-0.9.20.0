# 2017.08.29 21:46:28 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/DemountDeviceDialog.py
from gui.Scaleform.daapi.view.dialogs import DIALOG_BUTTON_ID
from gui.Scaleform.daapi.view.dialogs.IconPriceDialog import IconPriceDialog

class DemountDeviceDialog(IconPriceDialog):

    def __init__(self, meta, handler):
        super(IconPriceDialog, self).__init__(meta, handler)
        self._meta.onConfirmationStatusChnaged += self.__confirmationStatusChangeHandler

    def _populate(self):
        super(DemountDeviceDialog, self)._populate()
        self.__confirmationStatusChangeHandler(self._meta.isOperationAllowed)

    def __confirmationStatusChangeHandler(self, isAllowed):
        self.as_setOperationAllowedS(isAllowed)
        self.as_setButtonEnablingS(DIALOG_BUTTON_ID.SUBMIT, isAllowed)
        if not isAllowed:
            self.as_setButtonFocusS(DIALOG_BUTTON_ID.CLOSE)

    def _dispose(self):
        if self._meta is not None:
            self._meta.onConfirmationStatusChnaged -= self.__confirmationStatusChangeHandler
            self._meta.dispose()
        super(IconPriceDialog, self)._dispose()
        return
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\dialogs\DemountDeviceDialog.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:46:28 Støední Evropa (letní èas)
