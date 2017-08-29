# 2017.08.29 21:49:48 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/validators.py
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.server_events import IEventsCache

def questHasThisAchievementAsBonus(name, block):
    eventsCache = dependency.instance(IEventsCache)
    for records in eventsCache.getQuestsDossierBonuses().itervalues():
        if (block, name) in records:
            return True

    return False


def alreadyAchieved(achievementClass, name, block, dossier):
    return achievementClass.checkIsInDossier(block, name, dossier)


def requiresFortification():
    lobbyContext = dependency.instance(ILobbyContext)
    return lobbyContext.getServerSettings() is not None and lobbyContext.getServerSettings().isStrongholdsEnabled()


def accountIsRoaming(dossier):
    return dossier.isInRoaming()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\validators.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:49:48 Støední Evropa (letní èas)
