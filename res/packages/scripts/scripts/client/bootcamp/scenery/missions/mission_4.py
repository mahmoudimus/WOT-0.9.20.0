# 2017.08.29 21:43:54 Støední Evropa (letní èas)
# Embedded file name: scripts/client/bootcamp/scenery/missions/mission_4.py
from bootcamp.scenery.AbstractMission import AbstractMission

class Mission4(AbstractMission):

    def __init__(self, assistant):
        super(Mission4, self).__init__(assistant)

    def destroy(self):
        super(Mission4, self).destroy()

    def start(self):
        super(Mission4, self).start()
        self.playSound2D('vo_bc_main_task')
        self.playSound2D('bc_main_tips_task_start')
        self._avatar.muteSounds(('crew_member_contusion', 'track_destroyed', 'fire_started', 'gunner_killed'))

    def update(self):
        super(Mission4, self).update()

    def onPlayerDetectEnemy(self, new, lost):
        self._playCombatMusic()

    def stop(self):
        self._avatar.muteSounds(())
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\bootcamp\scenery\missions\mission_4.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:43:54 Støední Evropa (letní èas)
