# 2017.08.29 21:48:34 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/ContainerManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ContainerManagerMeta(BaseDAAPIComponent):

    def isModalViewsIsExists(self):
        self._printOverrideError('isModalViewsIsExists')

    def as_getViewS(self, name):
        if self._isDAAPIInited():
            return self.flashObject.as_getView(name)

    def as_showS(self, name, x = 0, y = 0):
        if self._isDAAPIInited():
            return self.flashObject.as_show(name, x, y)

    def as_registerContainerS(self, containerType, name):
        if self._isDAAPIInited():
            return self.flashObject.as_registerContainer(containerType, name)

    def as_unregisterContainerS(self, containerType):
        if self._isDAAPIInited():
            return self.flashObject.as_unregisterContainer(containerType)

    def as_closePopUpsS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_closePopUps()

    def as_isOnTopS(self, cType, vName):
        if self._isDAAPIInited():
            return self.flashObject.as_isOnTop(cType, vName)

    def as_bringToFrontS(self, cType, vName):
        if self._isDAAPIInited():
            return self.flashObject.as_bringToFront(cType, vName)

    def as_showContainersS(self, viewTypes):
        """
        :param viewTypes: Represented by Vector.<String> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showContainers(viewTypes)

    def as_hideContainersS(self, viewTypes):
        """
        :param viewTypes: Represented by Vector.<String> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_hideContainers(viewTypes)

    def as_isContainerShownS(self, viewType):
        if self._isDAAPIInited():
            return self.flashObject.as_isContainerShown(viewType)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\framework\entities\abstract\ContainerManagerMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:35 St�edn� Evropa (letn� �as)
