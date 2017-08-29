# 2017.08.29 21:46:19 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCBattleSpaceEnv.py
from gui.sounds.ambients import BattleSpaceEnv, NoMusic

class BCBattleSpaceEnv(BattleSpaceEnv):

    def stop(self):
        self._music = NoMusic()
        self._onChanged()
        super(BCBattleSpaceEnv, self).stop()

    def _setAfterBattleAmbient(self):
        pass
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\bootcamp\BCBattleSpaceEnv.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:46:19 Støední Evropa (letní èas)
