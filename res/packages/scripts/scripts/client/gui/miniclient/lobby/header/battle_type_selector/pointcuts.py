# 2017.08.29 21:45:15 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/miniclient/lobby/header/battle_type_selector/pointcuts.py
from helpers import aop
import aspects

class _BattleItemSelector(aop.Pointcut):

    def __init__(self, battleTypeBuilderMethod, aspects_):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.header', 'battle_selector_items', battleTypeBuilderMethod, aspects=aspects_)


class RankedBattle(_BattleItemSelector):

    def __init__(self):
        _BattleItemSelector.__init__(self, '_addRankedBattleType', (aspects.RankedBattle,))


class CommandBattle(_BattleItemSelector):

    def __init__(self):
        _BattleItemSelector.__init__(self, '_addCommandBattleType', (aspects.CommandBattle,))


class TrainingBattle(_BattleItemSelector):

    def __init__(self):
        _BattleItemSelector.__init__(self, '_addTrainingBattleType', (aspects.TrainingBattle,))


class SpecialBattle(_BattleItemSelector):

    def __init__(self):
        _BattleItemSelector.__init__(self, '_addSpecialBattleType', (aspects.SpecialBattle,))


class FalloutBattle(_BattleItemSelector):

    def __init__(self):
        _BattleItemSelector.__init__(self, '_addFalloutBattleType', (aspects.FalloutBattle,))


class StrongholdBattle(_BattleItemSelector):

    def __init__(self):
        _BattleItemSelector.__init__(self, '_addStrongholdsBattleType', (aspects.StrongholdBattle,))


class OnBattleTypeSelectorPopulate(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.header.BattleTypeSelectPopover', 'BattleTypeSelectPopover', '_populate', aspects=(aspects.OnBattleTypeSelectorPopulate,))
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\miniclient\lobby\header\battle_type_selector\pointcuts.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:45:15 Støední Evropa (letní èas)
