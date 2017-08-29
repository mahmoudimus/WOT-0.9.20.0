# 2017.08.29 21:43:54 Støední Evropa (letní èas)
# Embedded file name: scripts/client/bootcamp/scenery/missions/mission_5.py
from constants import ARENA_PERIOD
from helpers.CallbackDelayer import CallbackDelayer
from bootcamp.scenery.AbstractMission import AbstractMission

class Mission5(AbstractMission):

    def __init__(self, assistant):
        super(Mission5, self).__init__(assistant)
        self.__musicCallback = CallbackDelayer()

    def destroy(self):
        super(Mission5, self).destroy()

    def start(self):
        super(Mission5, self).start()
        self.playSound2D('vo_bc_main_task')
        self.playSound2D('bc_main_tips_task_start')

    def update(self):
        super(Mission5, self).update()

    def _onPeriodChange(self, *args):
        super(Mission5, self)._onPeriodChange(*args)
        if args[0] == ARENA_PERIOD.BATTLE:
            self._playCombatMusic()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\bootcamp\scenery\missions\mission_5.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:43:55 Støední Evropa (letní èas)
