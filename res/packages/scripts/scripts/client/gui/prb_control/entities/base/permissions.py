# 2017.08.29 21:45:22 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/prb_control/entities/base/permissions.py


class IPrbPermissions(object):
    """
    Base prebattle permission interface.
    """

    def canExitFromQueue(self):
        """
        Can player exit from queue
        """
        return True

    def canChangeVehicle(self):
        """
        Can player change vehicle
        """
        return True

    def canSendInvite(self):
        """
        Can player send an invite
        """
        return False

    def canCreateSquad(self):
        """
        Can player create squad
        """
        return False
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\base\permissions.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:45:22 Støední Evropa (letní èas)
