# 2017.08.29 21:49:46 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/PrematureDetonationAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SimpleProgressAchievement

class PrematureDetonationAchievement(SimpleProgressAchievement):

    def __init__(self, dossier, value = None):
        super(PrematureDetonationAchievement, self).__init__('prematureDetonationMedal', _AB.TEAM_7X7, dossier, value)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, 'prematureDetonation')
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\PrematureDetonationAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:49:46 St�edn� Evropa (letn� �as)
