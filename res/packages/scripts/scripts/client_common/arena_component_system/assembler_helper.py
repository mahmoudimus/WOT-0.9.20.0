# 2017.08.29 21:52:14 Støední Evropa (letní èas)
# Embedded file name: scripts/client_common/arena_component_system/assembler_helper.py
from constants import ARENA_BONUS_TYPE
from arena_component_system.epic_random_battle_component_assembler import EpicRandomBattleComponentAssembler
COMPONENT_ASSEMBLER = {ARENA_BONUS_TYPE.EPIC_RANDOM: EpicRandomBattleComponentAssembler,
 ARENA_BONUS_TYPE.EPIC_RANDOM_TRAINING: EpicRandomBattleComponentAssembler}
ARENA_BONUS_TYPE_CAP_COMPONENTS = {}
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client_common\arena_component_system\assembler_helper.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:52:14 Støední Evropa (letní èas)
