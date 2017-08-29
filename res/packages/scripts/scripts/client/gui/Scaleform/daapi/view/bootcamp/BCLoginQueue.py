# 2017.08.29 21:46:21 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCLoginQueue.py
from gui.Scaleform.daapi.view.meta.LoginQueueWindowMeta import LoginQueueWindowMeta
from gui.prb_control import prbDispatcherProperty
from gui.prb_control.entities.base.ctx import PrbAction, LeavePrbAction
from PlayerEvents import g_playerEvents
from gui.shared.events import ArgsEvent, BCLoginEvent
from gui.shared.event_bus import EVENT_BUS_SCOPE
from adisp import process

class BCLoginQueue(LoginQueueWindowMeta):

    def __init__(self, title, message, cancelLabel, _):
        super(BCLoginQueue, self).__init__()
        self.__updateData(title, message, cancelLabel)

    @prbDispatcherProperty
    def prbDispatcher(self):
        return None

    def __updateData(self, title, message, cancelLabel):
        self.__title = title
        self.__message = message
        self.__cancelLabel = cancelLabel

    def __updateTexts(self):
        self.as_setTitleS(self.__title)
        self.as_setMessageS(self.__message)
        self.as_setCancelLabelS(self.__cancelLabel)
        self.as_showAutoLoginBtnS(False)

    def _populate(self):
        super(BCLoginQueue, self)._populate()
        self.__updateTexts()
        self.addListener(ArgsEvent.UPDATE_ARGS, self.__onUpdateArgs, scope=EVENT_BUS_SCOPE.LOBBY)
        self.addListener(BCLoginEvent.CLOSE_WINDOW, self.__onWindowClose, scope=EVENT_BUS_SCOPE.LOBBY)
        g_playerEvents.onAccountBecomeNonPlayer += self.onAccountBecomeNonPlayer

    def _dispose(self):
        self.removeListener(ArgsEvent.UPDATE_ARGS, self.__onUpdateArgs, scope=EVENT_BUS_SCOPE.LOBBY)
        self.removeListener(BCLoginEvent.CLOSE_WINDOW, self.__onWindowClose, scope=EVENT_BUS_SCOPE.LOBBY)
        g_playerEvents.onAccountBecomeNonPlayer -= self.onAccountBecomeNonPlayer
        super(BCLoginQueue, self)._dispose()

    def onAccountBecomeNonPlayer(self):
        self.destroy()

    @process
    def onCancelClick(self):
        if self.prbDispatcher is not None:
            yield self.prbDispatcher.doLeaveAction(LeavePrbAction())
        self.fireEvent(BCLoginEvent(BCLoginEvent.CANCEL_WAITING), scope=EVENT_BUS_SCOPE.LOBBY)
        self.destroy()
        return

    def __onUpdateArgs(self, event):
        ctx = event.ctx
        if event.alias == self.alias:
            self.__updateData(**ctx)
            self.__updateTexts()

    def __onWindowClose(self, _):
        self.destroy()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\bootcamp\BCLoginQueue.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:46:21 St�edn� Evropa (letn� �as)
