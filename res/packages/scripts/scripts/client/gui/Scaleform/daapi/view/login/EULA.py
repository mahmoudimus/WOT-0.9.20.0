# 2017.08.29 21:47:56 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/login/EULA.py
import BigWorld
from gui import DialogsInterface
from gui.Scaleform.daapi.view.meta.EULAMeta import EULAMeta
from gui.Scaleform.daapi.view.dialogs import DIALOG_BUTTON_ID
from gui.shared.events import CloseWindowEvent, OpenLinkEvent
from helpers import dependency
from skeletons.connection_mgr import IConnectionManager

class EULADlg(EULAMeta):
    connectionMgr = dependency.descriptor(IConnectionManager)

    def __init__(self, ctx = None):
        super(EULADlg, self).__init__()
        self.__applied = False
        self.__eulaString = ctx.get('text', '')

    def _populate(self):
        super(EULADlg, self)._populate()
        self.connectionMgr.onDisconnected += self.__onDisconnected

    def _dispose(self):
        super(EULADlg, self)._dispose()
        self.connectionMgr.onDisconnected -= self.__onDisconnected
        self.__eulaString = None
        return

    def onWindowClose(self):
        if not self.__applied:
            DialogsInterface.showI18nConfirmDialog('quit', self.__onConfirmClosed, focusedID=DIALOG_BUTTON_ID.CLOSE)
        else:
            self.destroy()

    def requestEULAText(self):
        self.as_setEULATextS(self.__eulaString)

    def onApply(self):
        self.__applied = True
        self.__fireEulaClose()
        self.onWindowClose()

    def onLinkClick(self, url):
        self.fireEvent(OpenLinkEvent(OpenLinkEvent.SPECIFIED, url))

    def __onQuitOk(self):
        self.__fireEulaClose()
        self.destroy()
        BigWorld.quit()

    def __fireEulaClose(self):
        self.fireEvent(CloseWindowEvent(CloseWindowEvent.EULA_CLOSED, self.__applied))

    def __onConfirmClosed(self, isOk):
        if isOk:
            self.__onQuitOk()

    def __onDisconnected(self):
        self.__fireEulaClose()
        self.destroy()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\login\EULA.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:47:56 St�edn� Evropa (letn� �as)
