# 2017.08.29 21:53:17 Støední Evropa (letní èas)
# Embedded file name: scripts/common/items/sabaton_crew.py
from items import tankmen
SABATON_VEH_NAME = 'sweden:S23_Strv_81_sabaton'

def isSabatonCrew(tankmanDescr):
    return tankmen.hasTagInTankmenGroup(tankmanDescr.nationID, tankmanDescr.gid, tankmanDescr.isPremium, SABATON_VEH_NAME)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\items\sabaton_crew.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:53:17 Støední Evropa (letní èas)
