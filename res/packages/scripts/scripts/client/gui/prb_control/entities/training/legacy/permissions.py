# 2017.08.29 21:45:42 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/prb_control/entities/training/legacy/permissions.py
from constants import PREBATTLE_ROLE
from gui.prb_control.entities.base.legacy.permissions import LegacyPermissions

class TrainingPermissions(LegacyPermissions):
    """
    Training permissions class
    """

    def canChangeVehicle(self):
        return True

    @classmethod
    def isCreator(cls, roles):
        return roles == PREBATTLE_ROLE.TRAINING_CREATOR

    def canChangeSetting(self):
        return self.canChangeComment() or self.canChangeArena() or self.canMakeOpenedClosed()

    def canStartBattle(self):
        return self.canSetTeamState(1) and self.canSetTeamState(2)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\training\legacy\permissions.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:45:42 Støední Evropa (letní èas)
