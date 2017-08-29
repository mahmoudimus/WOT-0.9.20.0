# 2017.08.29 21:46:18 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCAppearManager.py
from gui.Scaleform.daapi.view.meta.BCAppearManagerMeta import BCAppearManagerMeta
from debug_utils import LOG_DEBUG
from bootcamp.BootCampEvents import g_bootcampEvents

class BCAppearManager(BCAppearManagerMeta):

    def __init__(self):
        LOG_DEBUG('BCAppearManagerPy.__init__')
        super(BCAppearManager, self).__init__()

    def _dispose(self):
        LOG_DEBUG('BCAppearManagerPy._dispose')
        super(BCAppearManager, self)._dispose()

    def onComponentTweenComplete(self, componentId):
        LOG_DEBUG('BCAppearManagerPy.onCoomponentTweenComplete', componentId)

    def onComponentPrepareAppear(self, componentId):
        LOG_DEBUG('BCAppearManagerPy.onComponentPrepareAppear', componentId)
        g_bootcampEvents.onComponentAppear(componentId)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\bootcamp\BCAppearManager.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:46:18 St�edn� Evropa (letn� �as)
