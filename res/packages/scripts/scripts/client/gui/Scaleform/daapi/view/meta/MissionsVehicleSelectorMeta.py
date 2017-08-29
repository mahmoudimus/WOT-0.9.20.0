# 2017.08.29 21:48:17 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MissionsVehicleSelectorMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class MissionsVehicleSelectorMeta(BaseDAAPIComponent):

    def as_setInitDataS(self, data):
        """
        :param data: Represented by MissionVehicleSelectorVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_showSelectedVehicleS(self, vehData):
        """
        :param vehData: Represented by VehicleCarouselVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showSelectedVehicle(vehData)

    def as_hideSelectedVehicleS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideSelectedVehicle()

    def as_closeS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_close()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\MissionsVehicleSelectorMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:17 Støední Evropa (letní èas)
