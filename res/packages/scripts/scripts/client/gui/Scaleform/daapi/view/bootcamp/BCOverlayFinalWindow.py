# 2017.08.29 21:46:21 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCOverlayFinalWindow.py
from gui.Scaleform.daapi.view.meta.BCOverlayFinalWindowMeta import BCOverlayFinalWindowMeta
import BigWorld

class BCOverlayFinalWindow(BCOverlayFinalWindowMeta):

    def __init__(self, settings):
        super(BCOverlayFinalWindow, self).__init__()

    def _populate(self):
        super(BCOverlayFinalWindow, self)._populate()
        from gui.app_loader.settings import APP_NAME_SPACE
        from gui.app_loader import g_appLoader
        g_appLoader.detachCursor(APP_NAME_SPACE.SF_BATTLE)
        from bootcamp.Bootcamp import g_bootcamp
        resultType, _, resultTypeStr, _, _ = g_bootcamp.getBattleResults()
        from debug_utils_bootcamp import LOG_DEBUG_DEV_BOOTCAMP
        LOG_DEBUG_DEV_BOOTCAMP('BCOverlayFinalWindow', resultType)
        self.as_msgTypeHandlerS(resultType, resultTypeStr)

    def _dispose(self):
        super(BCOverlayFinalWindow, self)._dispose()

    def animFinish(self):
        BigWorld.player().showBattleResults()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\bootcamp\BCOverlayFinalWindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:46:21 Støední Evropa (letní èas)
