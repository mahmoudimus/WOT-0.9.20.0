# 2017.08.29 21:43:53 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/bootcamp/scenery/missions/mission_1.py
import BigWorld
from bootcamp.scenery.AbstractMission import AbstractMission
import SoundGroups
from constants import ARENA_PERIOD

class Mission1(AbstractMission):

    def __init__(self, assistant):
        super(Mission1, self).__init__(assistant)
        self.firstMarker = self.createMarker('moveHere_0')
        self.firstMarkerDelay = 0
        self.needToShowFirstMarker = True

    def destroy(self):
        self.firstMarker = None
        super(Mission1, self).destroy()
        return

    def start(self):
        self.needToShowFirstMarker = True
        self.firstMarkerDelay = BigWorld.time()
        self.firstMarker.hide(True)
        self.playSound2D('vo_bc_follow_hint')
        self.playSound2D('bc_main_tips_task_start')
        super(Mission1, self).start()

    def update(self):
        super(Mission1, self).update()
        if self.needToShowFirstMarker:
            hintDelay = 14
            if BigWorld.time() >= self.firstMarkerDelay + hintDelay:
                self.firstMarker.show()
                self.needToShowFirstMarker = False

    def onZoneTriggerActivated(self, name):
        if name == 'moveHere_0_trigger':
            self.needToShowFirstMarker = False
            self.firstMarker.hide()

    def _onPeriodChange(self, *args):
        super(Mission1, self)._onPeriodChange(*args)
        if args[0] == ARENA_PERIOD.BATTLE:
            self._playCombatMusic()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\bootcamp\scenery\missions\mission_1.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:43:53 St�edn� Evropa (letn� �as)
