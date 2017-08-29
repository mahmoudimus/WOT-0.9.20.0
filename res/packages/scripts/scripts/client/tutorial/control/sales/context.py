# 2017.08.29 21:51:51 Støední Evropa (letní èas)
# Embedded file name: scripts/client/tutorial/control/sales/context.py
from tutorial.control import context

class SalesStartReqs(context.StartReqs):

    def isEnabled(self):
        return True

    def prepare(self, ctx):
        pass

    def process(self, descriptor, ctx):
        return True
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\tutorial\control\sales\context.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:51:51 Støední Evropa (letní èas)
