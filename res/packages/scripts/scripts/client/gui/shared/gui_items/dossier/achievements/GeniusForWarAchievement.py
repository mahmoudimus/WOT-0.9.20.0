# 2017.08.29 21:49:43 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/GeniusForWarAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SimpleProgressAchievement

class GeniusForWarAchievement(SimpleProgressAchievement):

    def __init__(self, dossier, value = None):
        super(GeniusForWarAchievement, self).__init__('geniusForWarMedal', _AB.TEAM_7X7, dossier, value)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, 'geniusForWar')
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\GeniusForWarAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:49:43 St�edn� Evropa (letn� �as)