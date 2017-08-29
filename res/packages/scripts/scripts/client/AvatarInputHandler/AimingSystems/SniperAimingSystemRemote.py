# 2017.08.29 21:43:37 Støední Evropa (letní èas)
# Embedded file name: scripts/client/AvatarInputHandler/AimingSystems/SniperAimingSystemRemote.py
import BigWorld
from AvatarInputHandler.subfilters_constants import AVATAR_SUBFILTERS
from AvatarInputHandler.AimingSystems.SniperAimingSystem import SniperAimingSystem

class SniperAimingSystemRemote(SniperAimingSystem):

    def handleMovement(self, dx, dy):
        pass

    def update(self, deltaTime):
        super(SniperAimingSystemRemote, self).update(deltaTime)
        player = BigWorld.player()
        shotPoint = player.remoteCamera.shotPoint
        getVector3 = getattr(player.filter, 'getVector3', None)
        if getVector3 is not None:
            shotPoint = getVector3(AVATAR_SUBFILTERS.CAMERA_SHOT_POINT, BigWorld.serverTime())
        self.focusOnPos(shotPoint)
        super(SniperAimingSystemRemote, self).overrideZoom(float(player.remoteCamera.zoom))
        return

    def overrideZoom(self, zoom):
        return self.getZoom()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\AvatarInputHandler\AimingSystems\SniperAimingSystemRemote.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:43:37 Støední Evropa (letní èas)
