# 2017.08.29 21:45:56 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/epic_random/score_panel.py
from gui.Scaleform.daapi.view.meta.EpicRandomScorePanelMeta import EpicRandomScorePanelMeta
from gui.battle_control.controllers.team_health_bar_ctrl import ITeamHealthBarListener
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class EpicRandomScorePanel(EpicRandomScorePanelMeta, ITeamHealthBarListener):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def updateTeamHealthPercent(self, allyPercentage, enemyPercentage):
        self.as_setTeamHealthPercentagesS(allyPercentage, enemyPercentage)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\battle\epic_random\score_panel.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:45:56 Støední Evropa (letní èas)
