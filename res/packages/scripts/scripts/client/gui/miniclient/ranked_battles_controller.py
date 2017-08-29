# 2017.08.29 21:45:13 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/miniclient/ranked_battles_controller.py
from helpers import aop

class _ParametrizeInitAspect(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        return False


class InitRankedPointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.game_control.ranked_battles_controller', 'RankedBattlesController', 'isAvailable', aspects=(_ParametrizeInitAspect,))
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\miniclient\ranked_battles_controller.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:45:13 Støední Evropa (letní èas)
