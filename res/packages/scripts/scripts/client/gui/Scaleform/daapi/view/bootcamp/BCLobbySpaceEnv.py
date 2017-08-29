# 2017.08.29 21:46:21 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCLobbySpaceEnv.py
from gui.sounds.ambients import SoundEnv
from gui.sounds.ambients import NoMusic
from gui.sounds.ambients import NoAmbient

class BCLobbySpaceEnv(SoundEnv):

    def __init__(self, soundsCtrl):
        super(BCLobbySpaceEnv, self).__init__(soundsCtrl, 'lobby', music=NoMusic(), ambient=NoAmbient())
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\bootcamp\BCLobbySpaceEnv.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:46:21 Støední Evropa (letní èas)
