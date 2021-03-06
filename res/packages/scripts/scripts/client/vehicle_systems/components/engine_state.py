# 2017.08.29 21:52:05 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/vehicle_systems/components/engine_state.py
from random import uniform
from constants import ARENA_PERIOD

class EngineState(object):
    NORMAL = 0
    REPAIRED = 1
    CRITICAL = 2
    DESTROYED = 3


class EngineLoad(object):
    _STOPPED = 0
    _IDLE = 1
    _MEDIUM = 2
    _HIGH = 3


_StateConvertor = {'destroyed': EngineState.DESTROYED,
 'critical': EngineState.CRITICAL,
 'repaired': EngineState.REPAIRED,
 'normal': EngineState.NORMAL}

def getEngineStateFromName(stateName):
    return _StateConvertor.get(stateName, EngineState.NORMAL)


def checkEngineStart(detailedEngineState, period):
    if period == ARENA_PERIOD.BATTLE:
        detailedEngineState.startEngineWithDelay(0.1)


def notifyEngineOnArenaPeriodChange(detailedEngineState, period, periodEndTime, serverTime):
    if period == ARENA_PERIOD.PREBATTLE:
        maxTime = periodEndTime - serverTime
        maxTime = maxTime * 0.7 if maxTime > 0.0 else 1.0
        time = uniform(0.0, maxTime)
        detailedEngineState.startEngineWithDelay(time)
    elif period == ARENA_PERIOD.BATTLE:
        detailedEngineState.notifyBattleStarted()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\vehicle_systems\components\engine_state.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:52:05 St�edn� Evropa (letn� �as)
