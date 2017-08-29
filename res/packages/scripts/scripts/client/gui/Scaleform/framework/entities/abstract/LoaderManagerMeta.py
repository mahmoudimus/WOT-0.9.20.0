# 2017.08.29 21:48:35 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/LoaderManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class LoaderManagerMeta(BaseDAAPIComponent):

    def viewLoaded(self, alias, viewName, view):
        self._printOverrideError('viewLoaded')

    def viewLoadError(self, alias, viewName, text):
        self._printOverrideError('viewLoadError')

    def viewInitializationError(self, alias, viewName):
        self._printOverrideError('viewInitializationError')

    def viewLoadCanceled(self, alias, viewName):
        self._printOverrideError('viewLoadCanceled')

    def as_loadViewS(self, data):
        """
        :param data: Represented by LoadViewVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_loadView(data)

    def as_cancelLoadViewS(self, viewName):
        if self._isDAAPIInited():
            return self.flashObject.as_cancelLoadView(viewName)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\framework\entities\abstract\LoaderManagerMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:35 Støední Evropa (letní èas)
