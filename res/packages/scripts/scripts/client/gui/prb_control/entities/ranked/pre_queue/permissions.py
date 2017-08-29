# 2017.08.29 21:45:37 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/prb_control/entities/ranked/pre_queue/permissions.py
from constants import QUEUE_TYPE
from gui.prb_control.entities.base.pre_queue.permissions import PreQueuePermissions
from gui.prb_control.storages import prequeue_storage_getter

class RankedPermissions(PreQueuePermissions):

    def canCreateSquad(self):
        return False
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\ranked\pre_queue\permissions.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:45:37 Støední Evropa (letní èas)
