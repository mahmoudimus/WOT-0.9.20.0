# 2017.08.29 21:49:50 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/abstract/SeriesAchievement.py
import BigWorld
from RegularAchievement import RegularAchievement

class SeriesAchievement(RegularAchievement):

    def getMaxSeriesInfo(self):
        return (self._getCounterRecordNames()[1], self.getValue())

    def getI18nValue(self):
        return BigWorld.wg_getIntegralFormat(self._value)

    def _getCounterRecordNames(self):
        return (None, None)

    def _readValue(self, dossier):
        record = self._getCounterRecordNames()[1]
        if record is not None:
            return dossier.getRecordValue(*record)
        else:
            return 0

    def _readLevelUpTotalValue(self, dossier):
        return self._value + 1

    def _readLevelUpValue(self, dossier):
        record = self._getCounterRecordNames()[0]
        if record is not None:
            return self._lvlUpTotalValue - dossier.getRecordValue(*record)
        else:
            return 0
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\abstract\SeriesAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:49:50 Støední Evropa (letní èas)
