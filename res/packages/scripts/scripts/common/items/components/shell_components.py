# 2017.08.29 21:53:26 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/items/components/shell_components.py
from constants import SHELL_TYPES
from items.components import component_constants

class ShellType(object):
    __slots__ = ('name',)

    def __init__(self, name):
        super(ShellType, self).__init__()
        self.name = name

    def __repr__(self):
        return '{}()'.format(self.__class__.__name__)


class ArmorPiercingType(ShellType):
    """Class provides ARMOR_PIERCING_xxx specific configuration."""
    __slots__ = ('normalizationAngle', 'ricochetAngleCos')

    def __init__(self, name):
        super(ArmorPiercingType, self).__init__(name)
        self.normalizationAngle = component_constants.ZERO_FLOAT
        self.ricochetAngleCos = component_constants.ZERO_FLOAT

    def __repr__(self):
        return 'ArmorPiercingType(normalizationAngle={}, ricochetAngleCos={})'.format(self.normalizationAngle, self.ricochetAngleCos)


class HollowChargeType(ShellType):
    """Class provides HOLLOW_CHARGE specific configuration."""
    __slots__ = ('piercingPowerLossFactorByDistance', 'ricochetAngleCos')

    def __init__(self, name):
        super(HollowChargeType, self).__init__(name)
        self.piercingPowerLossFactorByDistance = component_constants.ZERO_FLOAT
        self.ricochetAngleCos = component_constants.ZERO_FLOAT

    def __repr__(self):
        return 'HollowChargeType(piercingPowerLossFactorByDistance={}, ricochetAngleCos={})'.format(self.piercingPowerLossFactorByDistance, self.ricochetAngleCos)


class HighExplosiveType(ShellType):
    """Class provides HIGH_EXPLOSIVE specific configuration."""
    __slots__ = ('explosionRadius', 'explosionDamageFactor', 'explosionDamageAbsorptionFactor', 'explosionEdgeDamageFactor')

    def __init__(self, name):
        super(HighExplosiveType, self).__init__(name)
        self.explosionRadius = component_constants.ZERO_FLOAT
        self.explosionDamageFactor = component_constants.ZERO_FLOAT
        self.explosionDamageAbsorptionFactor = component_constants.ZERO_FLOAT
        self.explosionEdgeDamageFactor = component_constants.ZERO_FLOAT

    def __repr__(self):
        return 'HighExplosiveType(explosionRadius={}, explosionDamageFactor={}, explosionDamageAbsorptionFactor={}, explosionEdgeDamageFactor={})'.format(self.explosionRadius, self.explosionDamageFactor, self.explosionDamageAbsorptionFactor, self.explosionEdgeDamageFactor)


class Stun(object):
    """Class provides stun configuration of shell."""
    __slots__ = ('stunRadius', 'stunDuration', 'stunFactor', 'guaranteedStunDuration', 'damageDurationCoeff', 'guaranteedStunEffect', 'damageEffectCoeff')

    def __init__(self):
        super(Stun, self).__init__()
        self.stunRadius = component_constants.ZERO_FLOAT
        self.stunDuration = component_constants.ZERO_FLOAT
        self.stunFactor = component_constants.ZERO_FLOAT
        self.guaranteedStunDuration = component_constants.ZERO_FLOAT
        self.damageDurationCoeff = component_constants.ZERO_FLOAT
        self.guaranteedStunEffect = component_constants.ZERO_FLOAT
        self.damageEffectCoeff = component_constants.ZERO_FLOAT

    def __repr__(self):
        return 'Stun(radius={}, duration={}, guaranteedDuration={}, damageDurationCoeff={} guaranteedSEffect={}, damageEffectCoeff={})'.format(self.stunRadius, self.stunDuration, self.guaranteedStunDuration, self.damageDurationCoeff, self.guaranteedStunEffect, self.damageEffectCoeff)


def createShellType(typeName):
    """Creates type-specific configuration of shell by name of type.
    :param typeName: string containing name of type. @see SHELL_TYPES.
    :return: instance of class that extends ShellType.
    """
    shellType = None
    if typeName in (SHELL_TYPES.ARMOR_PIERCING, SHELL_TYPES.ARMOR_PIERCING_HE, SHELL_TYPES.ARMOR_PIERCING_CR):
        shellType = ArmorPiercingType(typeName)
    elif typeName == SHELL_TYPES.HOLLOW_CHARGE:
        shellType = HollowChargeType(typeName)
    elif typeName == SHELL_TYPES.HIGH_EXPLOSIVE:
        shellType = HighExplosiveType(typeName)
    return shellType
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\items\components\shell_components.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:53:26 St�edn� Evropa (letn� �as)
