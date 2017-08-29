# 2017.08.29 21:42:46 Støední Evropa (letní èas)
# Embedded file name: scripts/client/AreaTrigger.py
import BigWorld
import TriggersManager

class AreaTrigger(BigWorld.UserDataObject):

    def __init__(self):
        BigWorld.UserDataObject.__init__(self)
        self.__id = TriggersManager.g_manager.addTrigger(TriggersManager.TRIGGER_TYPE.AREA, name=self.name, position=self.position, radius=self.radius, scale=self.scale, exitInterval=self.exitInterval, direction=self.direction)

    def destroy(self):
        TriggersManager.g_manager.delTrigger(self.__id)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\AreaTrigger.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:42:46 Støední Evropa (letní èas)
