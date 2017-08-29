# 2017.08.29 21:48:12 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FittingSelectPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class FittingSelectPopoverMeta(SmartPopOverView):

    def setVehicleModule(self, newId, oldId, isRemove):
        self._printOverrideError('setVehicleModule')

    def showModuleInfo(self, moduleId):
        self._printOverrideError('showModuleInfo')

    def setAutoRearm(self, autoRearm):
        self._printOverrideError('setAutoRearm')

    def buyVehicleModule(self, moduleId):
        self._printOverrideError('buyVehicleModule')

    def setCurrentTab(self, tabIndex):
        self._printOverrideError('setCurrentTab')

    def listOverlayClosed(self):
        self._printOverrideError('listOverlayClosed')

    def as_updateS(self, data):
        """
        :param data: Represented by FittingSelectPopoverVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_update(data)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\FittingSelectPopoverMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:12 Støední Evropa (letní èas)
