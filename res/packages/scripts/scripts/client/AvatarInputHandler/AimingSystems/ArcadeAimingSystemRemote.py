# 2017.08.29 21:43:37 Støední Evropa (letní èas)
# Embedded file name: scripts/client/AvatarInputHandler/AimingSystems/ArcadeAimingSystemRemote.py
import BigWorld
from AvatarInputHandler.subfilters_constants import AVATAR_SUBFILTERS
from AvatarInputHandler.AimingSystems.ArcadeAimingSystem import ArcadeAimingSystem

class ArcadeAimingSystemRemote(ArcadeAimingSystem):

    def handleMovement(self, dx, dy):
        if not BigWorld.player().isObserverFPV:
            super(ArcadeAimingSystemRemote, self).handleMovement(dx, dy)

    def update(self, deltaTime):
        super(ArcadeAimingSystemRemote, self).update(deltaTime)
        player = BigWorld.player()
        if player.isObserverFPV:
            shotPoint = player.remoteCamera.shotPoint
            zoom = player.remoteCamera.zoom
            getVector3 = getattr(player.filter, 'getVector3', None)
            if getVector3 is not None:
                shotPoint = getVector3(AVATAR_SUBFILTERS.CAMERA_SHOT_POINT, BigWorld.serverTime())
            self.focusOnPos(shotPoint)
            self.distanceFromFocus = zoom
        return
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\AvatarInputHandler\AimingSystems\ArcadeAimingSystemRemote.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:43:37 Støední Evropa (letní èas)
