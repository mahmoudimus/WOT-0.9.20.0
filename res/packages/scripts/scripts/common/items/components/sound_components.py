# 2017.08.29 21:53:26 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/items/components/sound_components.py
from collections import namedtuple
__all__ = ('SoundPair', 'StatedSounds', 'HullAimingSound', 'SoundSiegeModeStateChange', 'WWTripleSoundConfig')
SoundPair = namedtuple('SoundPair', ('PC', 'NPC'))
StatedSounds = namedtuple('StatedSound', ('state', 'underLimitSounds', 'overLimitSounds'))
HullAimingSound = namedtuple('HullAimingSound', ('lodDist', 'angleLimitValue', 'sounds'))
SoundSiegeModeStateChange = namedtuple('SoundSiegeModeStateChange', ['on', 'off'])

class WWTripleSoundConfig(object):
    __slots__ = ('__wwsound', '__wwsoundPC', '__wwsoundNPC')

    def __init__(self, wwsound, wwsoundPC, wwsoundNPC):
        super(WWTripleSoundConfig, self).__init__()
        self.__wwsound = wwsound
        self.__wwsoundPC = wwsoundPC
        self.__wwsoundNPC = wwsoundNPC

    @property
    def wwsound(self):
        """Gets string containing default name of sound."""
        return self.__wwsound

    @property
    def wwsoundPC(self):
        """Gets string containing default name of sound that relates to player."""
        return self.__wwsoundPC

    @property
    def wwsoundNPC(self):
        return self.__wwsoundNPC

    def isEmpty(self):
        return self.__wwsound == '' and (self.__wwsoundPC == '' or self.__wwsoundNPC == '')

    def getWWPlayerSound(self, isPersonal):
        if isPersonal:
            sound = self.__wwsoundPC
        else:
            sound = self.__wwsoundNPC
        if not sound:
            sound = self.__wwsound
        return sound
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\items\components\sound_components.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:53:26 St�edn� Evropa (letn� �as)
