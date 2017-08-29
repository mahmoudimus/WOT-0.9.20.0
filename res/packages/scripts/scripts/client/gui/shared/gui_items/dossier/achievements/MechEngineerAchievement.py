# 2017.08.29 21:49:45 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/MechEngineerAchievement.py
from dossiers2.custom.helpers import getMechanicEngineerRequirements
from abstract import NationSpecificAchievement
from abstract.mixins import HasVehiclesList
from helpers import dependency
from skeletons.gui.shared import IItemsCache

class MechEngineerAchievement(HasVehiclesList, NationSpecificAchievement):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, nationID, block, dossier, value = None):
        self.__vehTypeCompDescrs = self._parseVehiclesDescrsList(NationSpecificAchievement.makeFullName('mechanicEngineer', nationID), nationID, dossier)
        NationSpecificAchievement.__init__(self, 'mechanicEngineer', nationID, block, dossier, value)
        HasVehiclesList.__init__(self)

    def getVehiclesListTitle(self):
        return 'vehiclesToResearch'

    def isActive(self):
        return not len(self.getVehiclesData())

    def _readLevelUpValue(self, dossier):
        return len(self.getVehiclesData())

    def _getVehiclesDescrsList(self):
        return self.__vehTypeCompDescrs

    @classmethod
    def _parseVehiclesDescrsList(cls, name, nationID, dossier):
        if dossier is not None and dossier.isCurrentUser():
            return getMechanicEngineerRequirements(set(), cls.itemsCache.items.stats.unlocks, nationID).get(name, [])
        else:
            return []
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\gui_items\dossier\achievements\MechEngineerAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:49:45 St�edn� Evropa (letn� �as)
