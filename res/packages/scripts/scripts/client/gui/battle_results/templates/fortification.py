# 2017.08.29 21:44:47 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/battle_results/templates/fortification.py
from gui.battle_results.components import base
from gui.battle_results.components import common
from gui.battle_results.components import details
from gui.battle_results.components import personal
from gui.battle_results.components import shared
from gui.battle_results.components import vehicles
from gui.battle_results.templates import regular
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD
regular.FINISH_RESULT_VO_META.bind(common.StrongholdBattleFinishResultBlock)
STRONGHOLD_BATTLE_COMMON_STATS_BLOCK = regular.REGULAR_COMMON_STATS_BLOCK.clone()
STRONGHOLD_BATTLE_COMMON_STATS_BLOCK.addNextComponent(common.StrongholdBattleFinishResultBlock(None, '', _RECORD.PERSONAL, _RECORD.PERSONAL_AVATAR))
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\battle_results\templates\fortification.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:44:47 Støední Evropa (letní èas)
