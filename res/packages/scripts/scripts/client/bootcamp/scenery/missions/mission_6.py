# 2017.08.29 21:43:55 Støední Evropa (letní èas)
# Embedded file name: scripts/client/bootcamp/scenery/missions/mission_6.py
import BigWorld
from debug_utils_bootcamp import LOG_DEBUG_DEV_BOOTCAMP
import SoundGroups
from bootcamp.scenery.AbstractMission import AbstractMission

class Mission6(AbstractMission):

    def __init__(self, assistant):
        super(Mission6, self).__init__(assistant)

    def destroy(self):
        super(Mission6, self).destroy()

    def start(self):
        super(Mission6, self).start()
        self.playSound2D('bc_music_mission_06')
        self.playSound2D('vo_bc_main_task')

    def update(self):
        super(Mission6, self).update()

    def _onPeriodChange(self, *args):
        pass
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\bootcamp\scenery\missions\mission_6.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:43:55 Støední Evropa (letní èas)
