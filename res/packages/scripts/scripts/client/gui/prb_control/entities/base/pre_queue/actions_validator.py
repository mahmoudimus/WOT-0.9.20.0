# 2017.08.29 21:45:24 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/prb_control/entities/base/pre_queue/actions_validator.py
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator, ActionsValidatorComposite, CurrentVehicleActionsValidator
from gui.prb_control.items import ValidationResult

class InQueueValidator(BaseActionsValidator):
    """
    Is player in queue validator.
    """

    def _validate(self):
        if self._entity.isInQueue():
            return ValidationResult(False)
        return super(InQueueValidator, self)._validate()


class PreQueueActionsValidator(ActionsValidatorComposite):
    """
    Pre queue actions validator base class. It has several parts:
    - state validation
    - vehicle validation
    """

    def __init__(self, entity):
        self._stateValidator = self._createStateValidator(entity)
        self._vehiclesValidator = self._createVehiclesValidator(entity)
        validators = [self._stateValidator, self._vehiclesValidator]
        super(PreQueueActionsValidator, self).__init__(entity, validators)

    def _createStateValidator(self, entity):
        """
        Part of template method to build state validation part
        """
        return InQueueValidator(entity)

    def _createVehiclesValidator(self, entity):
        """
        Part of template method to build vehicles validation part
        """
        return CurrentVehicleActionsValidator(entity)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\base\pre_queue\actions_validator.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:45:25 Støední Evropa (letní èas)
