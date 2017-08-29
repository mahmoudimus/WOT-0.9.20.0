# 2017.08.29 21:48:11 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EpicRandomScorePanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class EpicRandomScorePanelMeta(BaseDAAPIComponent):

    def as_setTeamHealthPercentagesS(self, team1, team2):
        if self._isDAAPIInited():
            return self.flashObject.as_setTeamHealthPercentages(team1, team2)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\EpicRandomScorePanelMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:11 Støední Evropa (letní èas)
