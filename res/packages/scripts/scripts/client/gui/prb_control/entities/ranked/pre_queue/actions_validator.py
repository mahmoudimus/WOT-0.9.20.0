# 2017.08.29 21:45:37 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/prb_control/entities/ranked/pre_queue/actions_validator.py
from CurrentVehicle import g_currentVehicle
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator, ActionsValidatorComposite
from gui.prb_control.entities.base.pre_queue.actions_validator import PreQueueActionsValidator
from gui.prb_control.items import ValidationResult
from gui.prb_control.settings import PRE_QUEUE_RESTRICTION
from gui.ranked_battles.constants import PRIME_TIME_STATUS
from helpers import dependency
from skeletons.gui.game_control import IRankedBattlesController
from skeletons.gui.lobby_context import ILobbyContext

class RankedPrimeTimeValidator(BaseActionsValidator):
    """
    Ranked prime time validation
    """

    def _validate(self):
        rankedController = dependency.instance(IRankedBattlesController)
        status, _ = rankedController.getPrimeTimeStatus()
        if status != PRIME_TIME_STATUS.AVAILABLE:
            return ValidationResult(False, PRE_QUEUE_RESTRICTION.MODE_DISABLED)
        return super(RankedPrimeTimeValidator, self)._validate()


class RankedVehicleValidator(BaseActionsValidator):
    """
    Ranked vehicle validation
    """

    def _validate(self):
        lobbyContext = dependency.instance(ILobbyContext)
        vehicle = g_currentVehicle.item
        config = lobbyContext.getServerSettings().rankedBattles
        if vehicle.level < config.minLevel or vehicle.level > config.maxLevel:
            return ValidationResult(False, PRE_QUEUE_RESTRICTION.LIMIT_LEVEL, {'levels': range(config.minLevel, config.maxLevel + 1)})
        return super(RankedVehicleValidator, self)._validate()


class RankedActionsValidator(PreQueueActionsValidator):
    """
    Ranked actions validation class
    """

    def _createStateValidator(self, entity):
        baseValidator = super(RankedActionsValidator, self)._createStateValidator(entity)
        return ActionsValidatorComposite(entity, [baseValidator, RankedPrimeTimeValidator(entity)])

    def _createVehiclesValidator(self, entity):
        baseValidator = super(RankedActionsValidator, self)._createVehiclesValidator(entity)
        return ActionsValidatorComposite(entity, [baseValidator, RankedVehicleValidator(entity)])
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\ranked\pre_queue\actions_validator.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:45:37 St�edn� Evropa (letn� �as)
