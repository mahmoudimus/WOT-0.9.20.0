# 2017.08.29 21:48:34 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/ApplicationMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ApplicationMeta(BaseDAAPIComponent):

    def setLoaderMgr(self, mgr):
        self._printOverrideError('setLoaderMgr')

    def setGlobalVarsMgr(self, mgr):
        self._printOverrideError('setGlobalVarsMgr')

    def setSoundMgr(self, mgr):
        self._printOverrideError('setSoundMgr')

    def setContainerMgr(self, mgr):
        self._printOverrideError('setContainerMgr')

    def setContextMenuMgr(self, mgr):
        self._printOverrideError('setContextMenuMgr')

    def setPopoverMgr(self, mgr):
        self._printOverrideError('setPopoverMgr')

    def setColorSchemeMgr(self, mgr):
        self._printOverrideError('setColorSchemeMgr')

    def setEventLogMgr(self, mgr):
        self._printOverrideError('setEventLogMgr')

    def setTooltipMgr(self, mgr):
        self._printOverrideError('setTooltipMgr')

    def setVoiceChatMgr(self, mgr):
        self._printOverrideError('setVoiceChatMgr')

    def setUtilsMgr(self, mgr):
        self._printOverrideError('setUtilsMgr')

    def setTweenMgr(self, mgr):
        self._printOverrideError('setTweenMgr')

    def setGameInputMgr(self, mgr):
        self._printOverrideError('setGameInputMgr')

    def setCacheMgr(self, mgr):
        self._printOverrideError('setCacheMgr')

    def setTextMgr(self, mgr):
        self._printOverrideError('setTextMgr')

    def setTutorialMgr(self, mgr):
        self._printOverrideError('setTutorialMgr')

    def setImageManager(self, mgr):
        self._printOverrideError('setImageManager')

    def handleGlobalKeyEvent(self, command):
        self._printOverrideError('handleGlobalKeyEvent')

    def onAsInitializationCompleted(self):
        self._printOverrideError('onAsInitializationCompleted')

    def as_isDAAPIInitedS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_isDAAPIInited()

    def as_populateS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_populate()

    def as_disposeS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_dispose()

    def as_registerManagersS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_registerManagers()

    def as_setLibrariesListS(self, list):
        """
        :param list: Represented by Vector.<String> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setLibrariesList(list)

    def as_updateStageS(self, w, h, scale):
        if self._isDAAPIInited():
            return self.flashObject.as_updateStage(w, h, scale)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\framework\entities\abstract\ApplicationMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:34 St�edn� Evropa (letn� �as)
