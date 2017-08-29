# 2017.08.29 21:53:28 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/items/readers/sound_readers.py
import math
import ResMgr
from constants import IS_DEVELOPMENT
from debug_utils import LOG_DEBUG
from items import _xml
from items.components import component_constants
from items.components import sound_components
from items.readers import shared_readers

def readWWTripleSoundConfig(section):
    """Reads WW sound configuration of hull or engine that contains 3 names of sounds: default sound,
        sound for current player, sound for other players.
    :param section: instance of DataSection.
    :return: instance of WWTripleSoundConfig.
    """
    if IS_DEVELOPMENT:
        for name in ('sound', 'soundPC', 'soundNPC'):
            if section.has_key(name):
                raise ValueError('Section "[hull|engine]/{}" is no longer supported'.format(name))

    return sound_components.WWTripleSoundConfig(section.readString('wwsound', component_constants.EMPTY_STRING), section.readString('wwsoundPC', component_constants.EMPTY_STRING), section.readString('wwsoundNPC', component_constants.EMPTY_STRING))


def readHullAimingSound(xmlCtx, section, cache):
    if section['hullAiming'] is None:
        return
    else:
        try:
            lodDist = shared_readers.readLodDist(xmlCtx, section, 'hullAiming/audio/lodDist', cache)
            angleLimit = math.radians(_xml.readFloat(xmlCtx, section, 'hullAiming/audio/angleLimitValue', component_constants.ZERO_FLOAT))
            sounds = []
            for actionName, actionSection in _xml.getChildren(xmlCtx, section, 'hullAiming/audio/sounds'):
                ctx = (xmlCtx, 'hullAiming/audio/sounds')
                underLimitSouns = sound_components.SoundPair(PC=_xml.readNonEmptyString(ctx, actionSection, 'underLimitSounds/wwsoundPC'), NPC=_xml.readNonEmptyString(ctx, actionSection, 'underLimitSounds/wwsoundNPC'))
                overLimitSounds = sound_components.SoundPair(PC=_xml.readNonEmptyString(ctx, actionSection, 'overLimitSounds/wwsoundPC'), NPC=_xml.readNonEmptyString(ctx, actionSection, 'overLimitSounds/wwsoundNPC'))
                sound = sound_components.StatedSounds(state=actionName, underLimitSounds=underLimitSouns, overLimitSounds=overLimitSounds)
                sounds.append(sound)

            hullAimingSound = sound_components.HullAimingSound(lodDist=lodDist, angleLimitValue=angleLimit, sounds=sounds)
            return hullAimingSound
        except:
            LOG_DEBUG('Incorrect hullAiming/audio section')
            return

        return


def readSoundSiegeModeStateChange(xmlCtx, section):
    """Reads soundStateChange section for siege mode.
    :param xmlCtx: tuple(root ctx or None, path to section).
    :param section: instance of DataSection.
    :return: instance of LeveredSuspensionConfig for levered suspension or None.
    """
    return sound_components.SoundSiegeModeStateChange(on=_xml.readStringOrNone(xmlCtx, section, 'soundStateChange/on'), off=_xml.readStringOrNone(xmlCtx, section, 'soundStateChange/off'))
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\items\readers\sound_readers.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:53:28 St�edn� Evropa (letn� �as)
