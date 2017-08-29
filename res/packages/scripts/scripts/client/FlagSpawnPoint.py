# 2017.08.29 21:42:59 Støední Evropa (letní èas)
# Embedded file name: scripts/client/FlagSpawnPoint.py
import BigWorld
from debug_utils import LOG_DEBUG

class FlagSpawnPoint(BigWorld.UserDataObject):

    def __init__(self):
        BigWorld.UserDataObject.__init__(self)
        LOG_DEBUG('FlagSpawnPoint ', self.position)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\FlagSpawnPoint.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:42:59 Støední Evropa (letní èas)
