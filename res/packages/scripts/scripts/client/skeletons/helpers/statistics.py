# 2017.08.29 21:51:40 Støední Evropa (letní èas)
# Embedded file name: scripts/client/skeletons/helpers/statistics.py


class IStatisticsCollector(object):

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def start(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError

    @property
    def update(self):
        raise NotImplementedError

    def getStatistics(self, andStop = True):
        raise NotImplementedError

    def noteHangarLoadingState(self, state, initialState = False, showSummaryNow = False):
        raise NotImplementedError
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\skeletons\helpers\statistics.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:51:40 Støední Evropa (letní èas)
