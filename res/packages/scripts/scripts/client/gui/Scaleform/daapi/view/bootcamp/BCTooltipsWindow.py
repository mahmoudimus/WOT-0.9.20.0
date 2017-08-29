# 2017.08.29 21:46:23 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCTooltipsWindow.py
from gui.Scaleform.daapi.view.meta.BCTooltipsWindowMeta import BCTooltipsWindowMeta

class BCTooltipsWindow(BCTooltipsWindowMeta):

    def __init__(self, settings):
        super(BCTooltipsWindow, self).__init__()
        self.__completed = settings['completed']
        self.__hideCallback = settings['hideCallback']

    def _populate(self):
        super(BCTooltipsWindow, self)._populate()
        if self.__completed:
            self.as_completeHandlerS()
        else:
            self.as_showHandlerS()

    def _dispose(self):
        super(BCTooltipsWindow, self)._dispose()

    def animFinish(self):
        if self.__hideCallback is not None:
            self.__hideCallback()
        return
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\bootcamp\BCTooltipsWindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:46:23 Støední Evropa (letní èas)
