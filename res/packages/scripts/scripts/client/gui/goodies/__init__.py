# 2017.08.29 21:45:10 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/goodies/__init__.py
from gui.goodies.goodies_cache import GoodiesCache
from skeletons.gui.goodies import IGoodiesCache
__all__ = ('getGoodiesCacheConfig',)

def getGoodiesCacheConfig(manager):
    """ Configures services for package goodies.
    :param manager: instance of dependency manager.
    """
    cache = GoodiesCache()
    cache.init()
    manager.addInstance(IGoodiesCache, cache, finalizer='fini')
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\goodies\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:45:10 Støední Evropa (letní èas)
