# 2017.08.29 21:48:36 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/TutorialManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class TutorialManagerMeta(BaseDAAPIComponent):

    def onComponentFound(self, componentId):
        self._printOverrideError('onComponentFound')

    def onComponentDisposed(self, componentId):
        self._printOverrideError('onComponentDisposed')

    def onTriggerActivated(self, componentId, triggerId):
        self._printOverrideError('onTriggerActivated')

    def as_setSystemEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSystemEnabled(value)

    def as_setDescriptionsS(self, descriptions):
        if self._isDAAPIInited():
            return self.flashObject.as_setDescriptions(descriptions)

    def as_setCriteriaS(self, criteriaName, criteriaValue):
        if self._isDAAPIInited():
            return self.flashObject.as_setCriteria(criteriaName, criteriaValue)

    def as_setTriggersS(self, componentId, triggers):
        """
        :param triggers: Represented by Array (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setTriggers(componentId, triggers)

    def as_showHintS(self, viewTutorialId, componentId, data, isCustomCmp = False):
        if self._isDAAPIInited():
            return self.flashObject.as_showHint(viewTutorialId, componentId, data, isCustomCmp)

    def as_hideHintS(self, viewTutorialId, componentId):
        if self._isDAAPIInited():
            return self.flashObject.as_hideHint(viewTutorialId, componentId)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\framework\entities\abstract\TutorialManagerMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:36 Støední Evropa (letní èas)
