# 2017.08.29 21:52:15 Støední Evropa (letní èas)
# Embedded file name: scripts/client_common/arena_component_system/epic_random_battle_component_assembler.py
from arena_component_system.client_arena_component_assembler import ClientArenaComponentAssembler
from arena_components.player_type_specific_components import getPlayerTypeSpecificComponentsForEpicRandom

class EpicRandomBattleComponentAssembler(ClientArenaComponentAssembler):

    @staticmethod
    def assembleComponents(componentSystem):
        ClientArenaComponentAssembler._assembleBonusCapsComponents(componentSystem)
        ClientArenaComponentAssembler._addArenaComponents(componentSystem, getPlayerTypeSpecificComponentsForEpicRandom())

    @staticmethod
    def disassembleComponents(componentSystem):
        pass
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client_common\arena_component_system\epic_random_battle_component_assembler.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:52:15 Støední Evropa (letní èas)
