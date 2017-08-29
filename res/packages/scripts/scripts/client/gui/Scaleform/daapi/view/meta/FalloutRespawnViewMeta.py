# 2017.08.29 21:48:12 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FalloutRespawnViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FalloutRespawnViewMeta(BaseDAAPIComponent):

    def onVehicleSelected(self, vehicleID):
        self._printOverrideError('onVehicleSelected')

    def onPostmortemBtnClick(self):
        self._printOverrideError('onPostmortemBtnClick')

    def as_initializeComponentS(self, mainData, slotsData):
        """
        :param mainData: Represented by FalloutRespawnViewVO (AS)
        :param slotsData: Represented by Vector.<VehicleSlotVO> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_initializeComponent(mainData, slotsData)

    def as_updateTimerS(self, mainTimer, slotsStateData):
        """
        :param slotsStateData: Represented by Vector.<VehicleStateVO> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateTimer(mainTimer, slotsStateData)

    def as_updateS(self, selectedVehicleName, slotsStateData):
        """
        :param slotsStateData: Represented by Vector.<VehicleStateVO> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_update(selectedVehicleName, slotsStateData)

    def as_showGasAttackModeS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showGasAttackMode()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\FalloutRespawnViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:12 Støední Evropa (letní èas)
