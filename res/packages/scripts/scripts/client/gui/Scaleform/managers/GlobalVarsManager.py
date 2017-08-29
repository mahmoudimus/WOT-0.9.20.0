# 2017.08.29 21:49:14 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/managers/GlobalVarsManager.py
import constants
from gui import GUI_SETTINGS
from gui.Scaleform.framework.entities.abstract.GlobalVarsMgrMeta import GlobalVarsMgrMeta
from helpers import getClientOverride, dependency
from skeletons.gui.game_control import IWalletController, ITradeInController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
from bootcamp.Bootcamp import g_bootcamp

class GlobalVarsManager(GlobalVarsMgrMeta):
    _isLoginLoadInfoRequested = False
    itemsCache = dependency.descriptor(IItemsCache)
    wallet = dependency.descriptor(IWalletController)
    tradeIn = dependency.descriptor(ITradeInController)
    lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self):
        super(GlobalVarsManager, self).__init__()

    def isDevelopment(self):
        return constants.IS_DEVELOPMENT

    def isShowLangaugeBar(self):
        return GUI_SETTINGS.isShowLanguageBar

    def isShowServerStats(self):
        return constants.IS_SHOW_SERVER_STATS

    def isChina(self):
        return constants.IS_CHINA

    def isKorea(self):
        return constants.IS_KOREA

    def isTutorialRunning(self, tutorialID):
        try:
            from tutorial.loader import isTutorialRunning
        except:

            def isTutorialRunning(_):
                return False

        return isTutorialRunning(tutorialID)

    def isFreeXpToTankman(self):
        return self.itemsCache.items.shop.freeXPToTManXPRate > 0

    def getLocaleOverride(self):
        return getClientOverride()

    def isRoamingEnabled(self):
        return self.lobbyContext.getServerSettings().roaming.isEnabled()

    def isInRoaming(self):
        return self.lobbyContext.getServerSettings().roaming.isInRoaming()

    def isWalletAvailable(self):
        if self.wallet:
            return self.wallet.isAvailable
        else:
            return False

    def isShowLoginRssFeed(self):
        return GUI_SETTINGS.loginRssFeed.show

    def isShowTicker(self):
        return constants.IS_CHINA and GUI_SETTINGS.movingText.show

    def isRentalsEnabled(self):
        return constants.IS_RENTALS_ENABLED

    def isPotapovQuestEnabled(self):
        return self.lobbyContext.getServerSettings().isPotapovQuestEnabled()

    def isLoginLoadedAtFirstTime(self):
        if GlobalVarsManager._isLoginLoadInfoRequested:
            return False
        else:
            GlobalVarsManager._isLoginLoadInfoRequested = True
            return True

    def isVehicleRestoreEnabled(self):
        return self.lobbyContext.getServerSettings().isVehicleRestoreEnabled()

    def isTradeInEnabled(self):
        return self.tradeIn.isEnabled()

    def isBootcampFinished(self):
        return g_bootcamp.isFinished()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\managers\GlobalVarsManager.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:49:14 St�edn� Evropa (letn� �as)
