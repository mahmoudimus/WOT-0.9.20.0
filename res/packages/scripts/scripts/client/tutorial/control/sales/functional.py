# 2017.08.29 21:51:51 Støední Evropa (letní èas)
# Embedded file name: scripts/client/tutorial/control/sales/functional.py
from gui.shared import g_eventBus, events
from tutorial.control.functional import FunctionalEffect

class LoadViewEffect(FunctionalEffect):

    def __init__(self, effect):
        self._isRunning = False
        super(LoadViewEffect, self).__init__(effect)

    def triggerEffect(self):
        viewData = self.getTarget()
        if viewData is not None:
            g_eventBus.handleEvent(events.LoadViewEvent(viewData.getAlias(), ctx=viewData.getCtx()), scope=viewData.getScope())
        return
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\tutorial\control\sales\functional.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:51:51 Støední Evropa (letní èas)
