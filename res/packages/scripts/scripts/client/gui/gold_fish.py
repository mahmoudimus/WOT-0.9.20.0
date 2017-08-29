# 2017.08.29 21:44:17 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/gold_fish.py
from account_helpers.AccountSettings import AccountSettings, GOLD_FISH_LAST_SHOW_TIME
import constants
from gui import GUI_SETTINGS
from helpers import dependency
from helpers.time_utils import getCurrentTimestamp
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache

@dependency.replace_none_kwargs(itemsCache=IItemsCache, lobbyContext=ILobbyContext)
def isGoldFishActionActive(itemsCache = None, lobbyContext = None):
    """Determines is the goldfish action is active at this moment for current type of account"""
    outOfSessionWallet = constants.ACCOUNT_ATTR.OUT_OF_SESSION_WALLET
    if itemsCache is None or lobbyContext is None:
        return False
    else:
        return not itemsCache.items.stats.isGoldFishBonusApplied and lobbyContext.getServerSettings().isGoldFishEnabled() and not itemsCache.items.stats.attributes & outOfSessionWallet != 0


def isTimeToShowGoldFishPromo():
    """Check is time has come to show GoldFish promo Window"""
    return getCurrentTimestamp() - AccountSettings.getFilter(GOLD_FISH_LAST_SHOW_TIME) >= GUI_SETTINGS.goldFishActionShowCooldown
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\gold_fish.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:44:17 St�edn� Evropa (letn� �as)
