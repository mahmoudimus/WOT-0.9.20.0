# 2017.08.29 21:49:32 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/__init__.py
from gui.shared.items_cache import ItemsCache
from gui.shared.event_bus import EventBus, EVENT_BUS_SCOPE
from gui.shared.gui_items.factories import GuiItemFactory
from skeletons.gui.shared import IItemsCache
from skeletons.gui.shared.gui_items import IGuiItemsFactory
__all__ = ('g_eventBus', 'getSharedServices', 'EVENT_BUS_SCOPE')
g_eventBus = EventBus()

def getSharedServices(manager):
    """ Configures services for package game_control.
    :param manager: instance of dependency manager.
    """
    cache = ItemsCache()
    cache.init()
    manager.addInstance(IItemsCache, cache, finalizer='fini')
    itemsFactory = GuiItemFactory()
    manager.addInstance(IGuiItemsFactory, itemsFactory)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:49:32 St�edn� Evropa (letn� �as)
