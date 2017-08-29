# 2017.08.29 21:45:48 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/ranked_battles/ranked_helpers.py
from helpers import dependency
from debug_utils import LOG_CURRENT_EXCEPTION
from skeletons.gui.lobby_context import ILobbyContext
from gui.ranked_battles.constants import RANKED_QUEST_ID_PREFIX

def getRankedDataFromTokenQuestID(questID):
    """
      parses id of quest for ranked seasons web league position:
      seasonID, cohort number and percent of people in given cohort
    """
    seasonID, cohort, percent = questID.split('_')[-3:]
    return (int(seasonID), int(cohort), int(percent))


def isRankedQuestID(ID):
    """
        checks whether given sting ID starts with proper prefix
    """
    return ID[:len(RANKED_QUEST_ID_PREFIX)] == RANKED_QUEST_ID_PREFIX


@dependency.replace_none_kwargs(lobbyContext=ILobbyContext)
def getRankedBattlesUrl(lobbyContext = None):
    if lobbyContext is None:
        return
    else:
        try:
            return lobbyContext.getServerSettings().bwRankedBattles.rblbHostUrl
        except AttributeError:
            LOG_CURRENT_EXCEPTION()
            return

        return
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\ranked_battles\ranked_helpers.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:45:48 St�edn� Evropa (letn� �as)
