# 2017.08.29 21:46:24 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/battle/bc_finish_sound_player.py
import SoundGroups
from PlayerEvents import g_playerEvents
from gui.Scaleform.daapi.view.battle.shared.finish_sound_player import FinishSoundPlayer
from gui.battle_control.view_components import IViewComponentsCtrlListener

class BCFinishSoundPlayer(FinishSoundPlayer, IViewComponentsCtrlListener):
    """ This is functionality that moved from BootcampFinishSoundController
    """

    def __init__(self):
        super(BCFinishSoundPlayer, self).__init__()
        self.__soundID = None
        g_playerEvents.onBootcampRoundFinished += self.__onBcRoundFinished
        return

    def detachedFromCtrl(self, ctrlID):
        g_playerEvents.onBootcampRoundFinished -= self.__onBcRoundFinished

    def _playSound(self, soundID):
        self.__soundID = soundID

    def __onBcRoundFinished(self):
        if self.__soundID:
            SoundGroups.g_instance.playSound2D(self.__soundID)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\bootcamp\battle\bc_finish_sound_player.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:46:24 Støední Evropa (letní èas)
