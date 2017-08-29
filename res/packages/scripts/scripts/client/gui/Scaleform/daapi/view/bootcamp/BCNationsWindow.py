# 2017.08.29 21:46:21 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCNationsWindow.py
from gui.Scaleform.daapi.view.meta.BCNationsWindowMeta import BCNationsWindowMeta
from bootcamp.Bootcamp import g_bootcamp
from debug_utils import LOG_DEBUG
from nations import INDICES as NATIONS_INDICES

class BCNationsWindow(BCNationsWindowMeta):

    def __init__(self, ctx = None):
        super(BCNationsWindow, self).__init__()
        self.__removedCallback = ctx['callback']

    def _populate(self):
        nationsOrder = [NATIONS_INDICES['usa'], NATIONS_INDICES['germany'], NATIONS_INDICES['ussr']]
        self.as_selectNationS(g_bootcamp.nation, nationsOrder)
        super(BCNationsWindow, self)._populate()

    def _dispose(self):
        super(BCNationsWindow, self)._dispose()

    def onNationShow(self, nationId):
        pass

    def onNationSelected(self, nationId):
        LOG_DEBUG('onNationSelected {0}'.format(nationId))
        g_bootcamp.changeNation(nationId, self.__removedCallback)
        self.destroy()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\bootcamp\BCNationsWindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:46:21 St�edn� Evropa (letn� �as)
