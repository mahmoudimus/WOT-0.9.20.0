# 2017.08.29 21:44:08 Støední Evropa (letní èas)
# Embedded file name: scripts/client/FX/ClientCompatibility.py
import BigWorld
if BigWorld.component == 'editor':

    def addMat(a, b):
        return 0


    def delMat(a):
        return 0


    BigWorld.addMat = addMat
    BigWorld.delMat = delMat

    def player():
        return None


    BigWorld.player = player
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\FX\ClientCompatibility.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:44:08 Støední Evropa (letní èas)
