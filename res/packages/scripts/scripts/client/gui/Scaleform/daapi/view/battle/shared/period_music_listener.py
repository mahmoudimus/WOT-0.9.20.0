# 2017.08.29 21:46:07 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/period_music_listener.py
import WWISE
from constants import ARENA_PERIOD
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView

class PeriodMusicListener(IAbstractPeriodView):
    """ This class serves to notify WWISE music engine about arena period changing
    """
    _ARENA_PERIOD_STATE = {ARENA_PERIOD.WAITING: 'STATE_arenastate_waiting',
     ARENA_PERIOD.PREBATTLE: 'STATE_arenastate_counter',
     ARENA_PERIOD.BATTLE: 'STATE_arenastate_battle'}
    _STATE_ID = 'STATE_arenastate'

    def setPeriod(self, period):
        state_value = self._ARENA_PERIOD_STATE.get(period, None)
        if state_value is not None:
            WWISE.WW_setState(self._STATE_ID, state_value)
        return
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\battle\shared\period_music_listener.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:46:07 St�edn� Evropa (letn� �as)
