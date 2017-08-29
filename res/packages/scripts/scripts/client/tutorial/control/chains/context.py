# 2017.08.29 21:51:46 Støední Evropa (letní èas)
# Embedded file name: scripts/client/tutorial/control/chains/context.py
from tutorial.control import context, game_vars
from tutorial.control.lobby.context import LobbyBonusesRequester

class ChainsStartReqs(context.StartReqs):

    def prepare(self, ctx):
        ctx.bonusCompleted = game_vars.getTutorialsCompleted()

    def process(self, descriptor, ctx):
        return True


class ChainsBonusesRequester(LobbyBonusesRequester):
    pass
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\tutorial\control\chains\context.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:51:47 Støední Evropa (letní èas)
