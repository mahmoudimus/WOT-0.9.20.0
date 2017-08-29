# 2017.08.29 21:52:46 Støední Evropa (letní èas)
# Embedded file name: scripts/common/unit_roster_config.py
from constants import IS_CHINA
from UnitRoster import BaseUnitRoster, BaseUnitRosterSlot, BaseUnitRosterLimits

class UnitRosterSlot(BaseUnitRosterSlot):
    DEFAULT_LEVELS = (6, 8)


class UnitRoster(BaseUnitRoster):
    MAX_SLOTS = 7
    MAX_CLOSED_SLOTS = 0
    SLOT_TYPE = UnitRosterSlot
    DEFAULT_SLOT_PACK = UnitRosterSlot().pack()
    MIN_UNIT_POINTS_SUM = 54
    MAX_UNIT_POINTS_SUM = 54
    MAX_UNIT_ASSEMBLER_ARTY = 2
    LIMITS_TYPE = BaseUnitRosterLimits


class RosterSlot6(BaseUnitRosterSlot):
    DEFAULT_LEVELS = (1, 6)


class RosterSlot8(BaseUnitRosterSlot):
    DEFAULT_LEVELS = (1, 8)


class RosterSlot10(BaseUnitRosterSlot):
    DEFAULT_LEVELS = (1, 10)


class SquadRoster(BaseUnitRoster):
    MAX_SLOTS = 3
    MAX_EMPTY_SLOTS = 2
    SLOT_TYPE = RosterSlot10
    DEFAULT_SLOT_PACK = RosterSlot10().pack()
    LIMITS_TYPE = BaseUnitRosterLimits


class FalloutClassicRoster(BaseUnitRoster):
    MAX_SLOTS = 3
    MAX_EMPTY_SLOTS = 2
    SLOT_TYPE = RosterSlot10
    DEFAULT_SLOT_PACK = RosterSlot10().pack()
    LIMITS_TYPE = BaseUnitRosterLimits
    MIN_VEHICLES = 3
    MAX_VEHICLES = 3


class FalloutMultiteamRoster(BaseUnitRoster):
    MAX_SLOTS = 3
    MAX_EMPTY_SLOTS = 1
    SLOT_TYPE = RosterSlot10
    DEFAULT_SLOT_PACK = RosterSlot10().pack()
    LIMITS_TYPE = BaseUnitRosterLimits
    MIN_VEHICLES = 1
    MAX_VEHICLES = 3


class SpecRoster(BaseUnitRoster):
    MAX_SLOTS = 15
    MAX_EMPTY_SLOTS = 14
    SLOT_TYPE = RosterSlot10
    DEFAULT_SLOT_PACK = RosterSlot10().pack()
    MAX_UNIT_POINTS_SUM = 150
    LIMITS_TYPE = BaseUnitRosterLimits


class EventRoster(BaseUnitRoster):
    MAX_SLOTS = 3
    MAX_EMPTY_SLOTS = 2
    SLOT_TYPE = RosterSlot10
    DEFAULT_SLOT_PACK = RosterSlot10().pack()
    LIMITS_TYPE = BaseUnitRosterLimits
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\unit_roster_config.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:52:46 Støední Evropa (letní èas)
