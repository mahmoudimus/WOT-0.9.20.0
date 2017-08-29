# 2017.08.29 21:43:38 Støední Evropa (letní èas)
# Embedded file name: scripts/client/AvatarInputHandler/AimingSystems/StrategicAimingSystemRemote.py
import BigWorld
from AvatarInputHandler.subfilters_constants import AVATAR_SUBFILTERS
from AvatarInputHandler.AimingSystems.StrategicAimingSystem import StrategicAimingSystem

class StrategicAimingSystemRemote(StrategicAimingSystem):

    def handleMovement(self, dx, dy):
        pass

    def update(self, deltaTime):
        super(StrategicAimingSystemRemote, self).update(deltaTime)
        player = BigWorld.player()
        shotPoint = player.remoteCamera.shotPoint
        getVector3 = getattr(player.filter, 'getVector3', None)
        if getVector3 is not None:
            shotPoint = getVector3(AVATAR_SUBFILTERS.CAMERA_SHOT_POINT, BigWorld.serverTime())
        self.updateTargetPos(shotPoint)
        super(StrategicAimingSystemRemote, self).overrideCamDist(player.remoteCamera.shotPoint.y)
        return

    def overrideCamDist(self, camDist):
        return self.getCamDist()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\AvatarInputHandler\AimingSystems\StrategicAimingSystemRemote.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:43:38 Støední Evropa (letní èas)
