# 2017.08.29 21:44:40 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/battle_results/stored_sorting.py
from account_helpers import AccountSettings
from account_helpers.AccountSettings import STATS_REGULAR_SORTING
from account_helpers.AccountSettings import STATS_SORTIE_SORTING
from constants import ARENA_BONUS_TYPE
__all__ = ('STATS_REGULAR_SORTING', 'STATS_SORTIE_SORTING', 'writeStatsSorting', 'readStatsSorting')

def writeStatsSorting(bonusType, iconType, sortDirection):
    key = STATS_REGULAR_SORTING
    value = {'iconType': iconType,
     'sortDirection': sortDirection}
    AccountSettings.setSettings(key, value)


def readStatsSorting(key):
    raise key in (STATS_REGULAR_SORTING, STATS_SORTIE_SORTING) or AssertionError('Key is invalid')
    settings = AccountSettings.getSettings(key)
    return (settings.get('iconType'), settings.get('sortDirection'))
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\battle_results\stored_sorting.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:44:40 Støední Evropa (letní èas)
