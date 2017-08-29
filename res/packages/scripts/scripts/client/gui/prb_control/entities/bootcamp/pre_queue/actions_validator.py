# 2017.08.29 21:45:31 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/prb_control/entities/bootcamp/pre_queue/actions_validator.py
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator
from gui.prb_control.items import ValidationResult

class BootcampActionsValidator(BaseActionsValidator):

    def _validate(self):
        from bootcamp.BootcampGarage import g_bootcampGarage
        if not g_bootcampGarage.isLessonFinished:
            return ValidationResult(False, 'bootcamp/lessonNotFinished')
        if not g_bootcampGarage.isSecondVehicleSelected():
            return ValidationResult(False, 'bootcamp/wrongVehicleSelected')
        return super(BootcampActionsValidator, self)._validate()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\bootcamp\pre_queue\actions_validator.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:45:31 Støední Evropa (letní èas)
