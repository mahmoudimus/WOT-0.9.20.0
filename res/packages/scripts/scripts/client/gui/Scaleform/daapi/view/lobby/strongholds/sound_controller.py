# 2017.08.29 21:47:42 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/strongholds/sound_controller.py
from gui.app_loader.decorators import sf_lobby
from gui.shared.SoundEffectsId import SoundEffectsId
import WWISE

class _StrongholdSoundController(object):

    @sf_lobby
    def app(self):
        return None

    def init(self):
        pass

    def fini(self):
        pass

    def playBattleRoomTimerAlert(self):
        self.__playSound(SoundEffectsId.BATTLE_ROOM_TIMER_ALERT)

    def __playSound(self, soundID):
        app = self.app
        if app is not None and app.soundManager is not None:
            app.soundManager.playEffectSound(soundID)
        return


g_strongholdSoundController = _StrongholdSoundController()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\strongholds\sound_controller.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:47:43 Støední Evropa (letní èas)
