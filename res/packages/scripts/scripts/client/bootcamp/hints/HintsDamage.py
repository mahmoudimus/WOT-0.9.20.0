# 2017.08.29 21:43:50 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/bootcamp/hints/HintsDamage.py
import TriggersManager
from constants import HINT_TYPE
from HintsBase import HintBase, HINT_COMMAND

class HintDamage(HintBase, TriggersManager.ITriggerListener):

    def __init__(self, avatar, hintId, triggerType, timeout):
        super(HintDamage, self).__init__(avatar, hintId, timeout)
        self._wasDamaged = False
        self._wasFixed = False
        self.__triggerType = triggerType
        self.__triggerId = None
        return

    def start(self):
        self._state = HintBase.STATE_DEFAULT
        self.__triggerId = TriggersManager.g_manager.addTrigger(self.__triggerType)
        TriggersManager.g_manager.addListener(self)

    def stop(self):
        self._state = HintBase.STATE_INACTIVE
        if TriggersManager.g_manager is not None:
            TriggersManager.g_manager.delTrigger(self.__triggerId)
            TriggersManager.g_manager.delListener(self)
        return

    def update(self):
        resultCommand = None
        if self._state == HintBase.STATE_DEFAULT:
            if self._wasDamaged:
                resultCommand = HINT_COMMAND.SHOW
                self._state = HintBase.STATE_HINT
        elif self._state == HintBase.STATE_HINT:
            if self._wasFixed:
                self._state = HintBase.STATE_COMPLETE
                resultCommand = HINT_COMMAND.HIDE
        elif self._state == HintBase.STATE_COMPLETE:
            self._wasDamaged = False
            self._wasFixed = False
            self._state = HintBase.STATE_INACTIVE
        return resultCommand

    def onTriggerActivated(self, args):
        if args['type'] == self.__triggerType and not self._wasDamaged:
            self._wasDamaged = True

    def onTriggerDeactivated(self, args):
        if args['type'] == self.__triggerType and not self._wasFixed:
            self._wasFixed = True


class HintCompositeDetrack(HintDamage):

    def __init__(self, avatar, params):
        super(HintCompositeDetrack, self).__init__(avatar, HINT_TYPE.HINT_REPAIR_TRACK, TriggersManager.TRIGGER_TYPE.PLAYER_VEHICLE_TRACKS_DAMAGED, params['timeout'])


class HintCompositeHealCommander(HintDamage):

    def __init__(self, avatar, params):
        super(HintCompositeHealCommander, self).__init__(avatar, HINT_TYPE.HINT_HEAL_CREW, TriggersManager.TRIGGER_TYPE.PLAYER_TANKMAN_SHOOTED, params['timeout'])


class HintCompositeBurn(HintDamage):

    def __init__(self, avatar, params):
        super(HintCompositeBurn, self).__init__(avatar, HINT_TYPE.HINT_USE_EXTINGUISHER, TriggersManager.TRIGGER_TYPE.PLAYER_VEHICLE_IN_FIRE, params['timeout'])
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\bootcamp\hints\HintsDamage.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:43:50 St�edn� Evropa (letn� �as)
