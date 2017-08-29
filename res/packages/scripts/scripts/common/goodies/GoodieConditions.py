# 2017.08.29 21:53:14 Støední Evropa (letní èas)
# Embedded file name: scripts/common/goodies/GoodieConditions.py


class Condition(object):

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def check(self, other):
        return self == other

    def __ne__(self, other):
        return not self.__eq__(other)


class MaxVehicleLevel(Condition):

    def __init__(self, level):
        self.level = level

    def __lt__(self, other):
        return self.level < other.level
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\goodies\GoodieConditions.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:53:14 Støední Evropa (letní èas)
