# 2017.08.29 21:51:39 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/skeletons/gui/shared/__init__.py
from Event import Event
from skeletons.gui.shared.utils import IItemsRequester, requesters

class IItemsCache(requesters.IRequester):
    onSyncStarted = None
    onSyncCompleted = None

    @property
    def waitForSync(self):
        raise NotImplementedError

    @property
    def items(self):
        raise NotImplementedError

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def clear(self):
        raise NotImplementedError

    def update(self, updateReason, diff = None, callback = None):
        raise NotImplementedError
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\skeletons\gui\shared\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:51:39 St�edn� Evropa (letn� �as)
