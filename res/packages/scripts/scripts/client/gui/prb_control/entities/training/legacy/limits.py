# 2017.08.29 21:45:42 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/prb_control/entities/training/legacy/limits.py
from CurrentVehicle import g_currentVehicle
from constants import PREBATTLE_ACCOUNT_STATE, PREBATTLE_TYPE
from gui.prb_control.entities.base.limits import AbstractTeamIsValid, LimitsCollection, VehicleIsValid
from gui.prb_control.entities.base.limits import TeamNoPlayersInBattle, TeamIsValid
from gui.prb_control.settings import PREBATTLE_RESTRICTION
from helpers import dependency
from items import vehicles
from skeletons.gui.shared import IItemsCache

class ObserverInTeamIsValid(AbstractTeamIsValid):
    """
    Observer's team limits
    """
    itemsCache = dependency.descriptor(IItemsCache)

    def check(self, rosters, team, teamLimits):
        accountsInfo = self._getAccountsInfo(rosters, team)
        if len(accountsInfo) < teamLimits['minCount']:
            return (False, 'limit/minCount')
        if self.__isAllObservers(accountsInfo):
            return (False, 'observers')
        return (True, '')

    @classmethod
    def __isAllObservers(cls, accountsInfo):
        """
        Checks are all players in team observers
        Args:
            accountsInfo: players accounts info
        """
        if not len(accountsInfo):
            return False
        for accInfo in accountsInfo.itervalues():
            if not accInfo['state'] & PREBATTLE_ACCOUNT_STATE.READY:
                continue
            if 'vehTypeCompDescr' not in accInfo or 'vehLevel' not in accInfo:
                vehDescr = vehicles.VehicleDescr(compactDescr=accInfo['vehCompDescr'])
                vehTypeCompDescr = vehDescr.type.compactDescr
            else:
                vehTypeCompDescr = accInfo['vehTypeCompDescr']
            if not cls.itemsCache.items.getItemByCD(vehTypeCompDescr).isObserver:
                return False

        return True


class TrainingVehicleIsValid(VehicleIsValid):
    """
    Class for current vehicle validation in trainings. Validates also:
    - is vehicle not observer
    """

    def check(self, teamLimits):
        isValid, restriction = super(TrainingVehicleIsValid, self).check(teamLimits)
        if isValid and g_currentVehicle.isObserver():
            return (False, PREBATTLE_RESTRICTION.VEHICLE_NOT_SUPPORTED)
        return (isValid, restriction)


class TrainingLimits(LimitsCollection):
    """
    Training limits class
    """

    def __init__(self, entity):
        super(TrainingLimits, self).__init__(entity, (TrainingVehicleIsValid(),), (TeamNoPlayersInBattle(PREBATTLE_TYPE.TRAINING), TeamIsValid(), ObserverInTeamIsValid()))
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\training\legacy\limits.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:45:42 St�edn� Evropa (letn� �as)
