# 2017.08.29 21:49:48 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/TitleSniperAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SeriesAchievement

class TitleSniperAchievement(SeriesAchievement):

    def __init__(self, dossier, value = None):
        super(TitleSniperAchievement, self).__init__('titleSniper', _AB.SINGLE, dossier, value)

    def _getCounterRecordNames(self):
        return ((_AB.TOTAL, 'sniperSeries'), (_AB.TOTAL, 'maxSniperSeries'))
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\TitleSniperAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:49:48 St�edn� Evropa (letn� �as)
