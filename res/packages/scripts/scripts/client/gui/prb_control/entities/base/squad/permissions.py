# 2017.08.29 21:45:26 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/prb_control/entities/base/squad/permissions.py
from gui.prb_control.entities.base.unit.permissions import UnitPermissions

class SquadPermissions(UnitPermissions):
    """
    Squad permission class
    """

    def canChangeLeadership(self):
        return True

    def canStealLeadership(self):
        return False

    def canExitFromQueue(self):
        return self.isCommander(self._roles)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\base\squad\permissions.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:45:26 St�edn� Evropa (letn� �as)
