# 2017.08.29 21:48:09 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CrewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class CrewMeta(BaseDAAPIComponent):

    def onShowRecruitWindowClick(self, rendererData, menuEnabled):
        self._printOverrideError('onShowRecruitWindowClick')

    def unloadAllTankman(self):
        self._printOverrideError('unloadAllTankman')

    def equipTankman(self, tankmanID, slot):
        self._printOverrideError('equipTankman')

    def updateTankmen(self):
        self._printOverrideError('updateTankmen')

    def openPersonalCase(self, value, tabNumber):
        self._printOverrideError('openPersonalCase')

    def onCrewDogMoreInfoClick(self):
        self._printOverrideError('onCrewDogMoreInfoClick')

    def onCrewDogItemClick(self):
        self._printOverrideError('onCrewDogItemClick')

    def as_tankmenResponseS(self, data):
        """
        :param data: Represented by TankmenResponseVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_tankmenResponse(data)

    def as_dogResponseS(self, dogName):
        if self._isDAAPIInited():
            return self.flashObject.as_dogResponse(dogName)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\CrewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:09 St�edn� Evropa (letn� �as)
