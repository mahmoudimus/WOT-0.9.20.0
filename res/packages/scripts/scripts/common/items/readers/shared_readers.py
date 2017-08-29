# 2017.08.29 21:53:28 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/items/readers/shared_readers.py
import ResMgr
from constants import IS_CLIENT, IS_BOT
from items import _xml
from items.components import component_constants
from items.components import shared_components
_ALLOWED_EMBLEM_SLOTS = component_constants.ALLOWED_EMBLEM_SLOTS

def readEmblemSlots(xmlCtx, section, subsectionName):
    """Reads section 'emblemSlots' to fetch sequence of emblem slots if they exist.
    :param xmlCtx: tuple(root ctx or None, path to section).
    :param section: instance of DataSection.
    :param subsectionName: string containing name of section to find slots configuration.
    :return: tuple containing EmblemSlot items.
    """
    slots = []
    for sname, subsection in _xml.getChildren(xmlCtx, section, subsectionName):
        if sname not in component_constants.ALLOWED_EMBLEM_SLOTS:
            _xml.raiseWrongXml(xmlCtx, 'emblemSlots/{}'.format(sname), 'expected {}'.format(_ALLOWED_EMBLEM_SLOTS))
        ctx = (xmlCtx, 'emblemSlots/{}'.format(sname))
        descr = shared_components.EmblemSlot(_xml.readVector3(ctx, subsection, 'rayStart'), _xml.readVector3(ctx, subsection, 'rayEnd'), _xml.readVector3(ctx, subsection, 'rayUp'), _xml.readPositiveFloat(ctx, subsection, 'size'), subsection.readBool('hideIfDamaged', False), _ALLOWED_EMBLEM_SLOTS[_ALLOWED_EMBLEM_SLOTS.index(sname)], subsection.readBool('isMirrored', False), subsection.readBool('isUVProportional', True), _xml.readIntOrNone(ctx, subsection, 'emblemId'))
        slots.append(descr)

    return tuple(slots)


def readLodDist(xmlCtx, section, subsectionName, cache):
    name = _xml.readNonEmptyString(xmlCtx, section, subsectionName)
    dist = cache.commonConfig['lodLevels'].get(name)
    if dist is None:
        _xml.raiseWrongXml(xmlCtx, subsectionName, "unknown lod level '%s'" % name)
    return dist


def readLodSettings(xmlCtx, section, cache):
    return shared_components.LodSettings(maxLodDistance=readLodDist(xmlCtx, section, 'lodSettings/maxLodDistance', cache), maxPriority=_xml.readIntOrNone(xmlCtx, section, 'lodSettings/maxPriority'))


def readSwingingSettings(xmlCtx, section, cache):
    """Reads section 'swinging' for each hull.
    :param xmlCtx: tuple(root ctx or None, path to section).
    :param section: instance of DataSection.
    :param cache: instance of vehicles.Cache.
    :return: instance of SwingingSettings.
    """
    return shared_components.SwingingSettings(readLodDist(xmlCtx, section, 'swinging/lodDist', cache), _xml.readNonNegativeFloat(xmlCtx, section, 'swinging/sensitivityToImpulse'), _xml.readTupleOfFloats(xmlCtx, section, 'swinging/pitchParams', 6), _xml.readTupleOfFloats(xmlCtx, section, 'swinging/rollParams', 7))


def readModels(xmlCtx, section, subsectionName):
    """Reads section with name 'subsectionName' to fetch paths of models
        for each hull, chassis, turret and gun.
    :param xmlCtx: tuple(root ctx or None, path to section).
    :param section: instance of DataSection.
    :param subsectionName: string containing name of desired section.
    :return: instance of ModelStatesPaths.
    """
    return shared_components.ModelStatesPaths(_xml.readNonEmptyString(xmlCtx, section, subsectionName + '/undamaged'), _xml.readNonEmptyString(xmlCtx, section, subsectionName + '/destroyed'), _xml.readNonEmptyString(xmlCtx, section, subsectionName + '/exploded'))


def readUserText(section):
    """Reads i18n information that contains user-friendly name, description of item.
    :param section: instance of DataSection.
    :return: instance of I18nComponent.
    """
    return shared_components.I18nComponent(section.readString('userString'), section.readString('description'), section.readString('shortUserString'))


def readDeviceHealthParams(xmlCtx, section, subsectionName = '', withHysteresis = True):
    """Reads health parameter for each device.
    :param xmlCtx: tuple(root ctx or None, path to section).
    :param section: instance of DataSection.
    :param subsectionName: string containing name of desired section or empty string
        if desired section is already exist.
    :param withHysteresis: if value equals True than read section 'hysteresisHealth',
        otherwise - do nothing.
    :return: instance of DeviceHealth.
    """
    if subsectionName:
        section = _xml.getSubsection(xmlCtx, section, subsectionName)
        xmlCtx = (xmlCtx, subsectionName)
    component = shared_components.DeviceHealth(_xml.readInt(xmlCtx, section, 'maxHealth', 1), _xml.readNonNegativeFloat(xmlCtx, section, 'repairCost'), _xml.readInt(xmlCtx, section, 'maxRegenHealth', 0))
    if component.maxRegenHealth > component.maxHealth:
        _xml.raiseWrongSection(xmlCtx, 'maxRegenHealth')
    if not IS_CLIENT and not IS_BOT:
        component.healthRegenPerSec = _xml.readNonNegativeFloat(xmlCtx, section, 'healthRegenPerSec')
        component.healthBurnPerSec = _xml.readNonNegativeFloat(xmlCtx, section, 'healthBurnPerSec')
        if section.has_key('chanceToHit'):
            component.chanceToHit = _xml.readFraction(xmlCtx, section, 'chanceToHit')
        else:
            component.chanceToHit = None
        if withHysteresis:
            hysteresisHealth = _xml.readInt(xmlCtx, section, 'hysteresisHealth', 0)
            if hysteresisHealth > component.maxRegenHealth:
                _xml.raiseWrongSection(xmlCtx, 'hysteresisHealth')
            component.hysteresisHealth = hysteresisHealth
    return component


def readCamouflage(xmlCtx, section, sectionName, default = None):
    """Reads camouflage configuration of vehicle's item on client-side only.
    :param xmlCtx: tuple(root ctx or None, path to section).
    :param section: instance of DataSection.
    :param sectionName:  string containing name of section.
    :param default: None or instance of Camouflage that is used as default.
    :return: instance of shared_components.Camouflage.
    """
    tilingKey = sectionName + '/tiling'
    if default is None or section.has_key(tilingKey):
        tiling = _xml.readTupleOfFloats(xmlCtx, section, tilingKey, 4)
        if tiling[0] <= 0 or tiling[1] <= 0:
            if default is None:
                _xml.raiseWrongSection(xmlCtx, tilingKey)
            else:
                tiling = default[0]
    else:
        tiling = default[0]
    maskKey = sectionName + '/exclusionMask'
    mask = section.readString(maskKey)
    if not mask and default is not None:
        mask = default[1]
    return shared_components.Camouflage(tiling, mask)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\items\readers\shared_readers.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:53:28 St�edn� Evropa (letn� �as)
