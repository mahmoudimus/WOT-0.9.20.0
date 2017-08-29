# 2017.08.29 21:49:33 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/formatters/tankmen.py
from helpers import dependency
from skeletons.gui.shared import IItemsCache

@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def formatDeletedTankmanStr(tankman, itemsCache = None):
    vehicle = itemsCache.items.getItemByCD(tankman.vehicleNativeDescr.type.compactDescr)
    return tankman.fullUserName + ' (%s, %s)' % (tankman.roleUserName, vehicle.userName)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\formatters\tankmen.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:49:33 Støední Evropa (letní èas)
