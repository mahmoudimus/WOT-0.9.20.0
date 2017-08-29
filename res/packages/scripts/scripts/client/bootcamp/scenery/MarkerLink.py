# 2017.08.29 21:43:53 Støední Evropa (letní èas)
# Embedded file name: scripts/client/bootcamp/scenery/MarkerLink.py
import Math
import BattleReplay

class MarkerLink(object):

    def __init__(self, markerName):
        self.name = markerName
        self.markerParams = None
        self.mm = None
        self.visible = True
        return

    def resolve(self, markerManager):
        self.markerManager = markerManager
        self.markerParams = self.markerManager.getMarkerParams(self.name)

    def show(self):
        if self.markerManager is not None and not self.visible:
            self.visible = True
            if not BattleReplay.g_replayCtrl.isPlaying:
                self.markerManager.showMarker(self.name)
        return

    def hide(self, silently = False):
        if self.markerManager is not None and self.visible:
            self.visible = False
            if not BattleReplay.g_replayCtrl.isPlaying:
                self.markerManager.hideMarker(self.name, silently)
        return

    position = property(lambda self: (self.markerParams['position'] if self.markerParams is not None else Math.Vector3(0.0, 0.0, 0.0)))
    isVisible = property(lambda self: self.visible)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\bootcamp\scenery\MarkerLink.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:43:53 Støední Evropa (letní èas)
