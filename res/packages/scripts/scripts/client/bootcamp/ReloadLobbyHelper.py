# 2017.08.29 21:43:48 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/bootcamp/ReloadLobbyHelper.py
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity
from gui.shared import EVENT_BUS_SCOPE
from gui.app_loader import g_appLoader
from gui.shared.events import AppLifeCycleEvent
from BootcampTransition import BootcampTransition

class ReloadLobbyHelper(EventSystemEntity):

    def __init__(self, finishCallback = None):
        super(ReloadLobbyHelper, self).__init__()
        self.__callback = finishCallback

    def reload(self):
        from gui.prb_control.dispatcher import g_prbLoader
        from gui.shared.personality import ServicesLocator
        self.addListener(AppLifeCycleEvent.INITIALIZED, self.__appInitialized, EVENT_BUS_SCOPE.GLOBAL)
        g_prbLoader.onAccountBecomeNonPlayer()
        ServicesLocator.gameState.onAvatarBecomePlayer()
        g_appLoader.switchAccountEntity()
        g_prbLoader.onAccountShowGUI({})
        BootcampTransition.start()

    def __onViewLoaded(self, view, loadParams):
        view.app.loaderManager.onViewLoaded -= self.__onViewLoaded
        BootcampTransition.stop()
        if self.__callback is not None:
            self.__callback()
        self.destroy()
        return

    def __appInitialized(self, event):
        self.app = g_appLoader.getApp(event.ns)
        self.app.loaderManager.onViewLoaded += self.__onViewLoaded
        self.removeListener(AppLifeCycleEvent.INITIALIZED, self.__appInitialized, EVENT_BUS_SCOPE.GLOBAL)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\bootcamp\ReloadLobbyHelper.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:43:49 St�edn� Evropa (letn� �as)
