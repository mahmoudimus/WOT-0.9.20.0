# 2017.08.29 21:47:52 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_compare/cmp_configurator_base.py
from gui.Scaleform.daapi.view.meta.VehicleCompareConfiguratorBaseViewMeta import VehicleCompareConfiguratorBaseViewMeta

class VehicleCompareConfiguratorBaseView(VehicleCompareConfiguratorBaseViewMeta):

    def __init__(self):
        super(VehicleCompareConfiguratorBaseView, self).__init__()
        self._container = None
        self.__isInited = False
        return

    def onShow(self):
        pass

    def onCamouflageUpdated(self):
        pass

    def onShellsUpdated(self, updateShells = False, selectedIndex = -1):
        pass

    def onOptDeviceUpdated(self):
        pass

    def onEquipmentUpdated(self):
        pass

    def onModulesUpdated(self):
        pass

    def onCrewSkillUpdated(self):
        pass

    def onCrewLevelUpdated(self, newLvl):
        pass

    def onResetToDefault(self):
        pass

    def setContainer(self, container):
        self._container = container
        self.__tryToInit()

    def _init(self):
        pass

    def _populate(self):
        super(VehicleCompareConfiguratorBaseView, self)._populate()
        self.__tryToInit()

    def _dispose(self):
        self._container = None
        super(VehicleCompareConfiguratorBaseView, self)._dispose()
        return

    def __tryToInit(self):
        if self.isCreated() and self._container is not None and not self.__isInited:
            self._init()
        return
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\vehicle_compare\cmp_configurator_base.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:47:52 St�edn� Evropa (letn� �as)
