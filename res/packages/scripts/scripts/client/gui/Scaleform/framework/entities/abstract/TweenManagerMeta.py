# 2017.08.29 21:48:36 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/TweenManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class TweenManagerMeta(BaseDAAPIComponent):

    def createTween(self, tween):
        self._printOverrideError('createTween')

    def disposeTween(self, tween):
        self._printOverrideError('disposeTween')

    def disposeAll(self):
        self._printOverrideError('disposeAll')

    def as_setDataFromXmlS(self, data):
        """
        :param data: Represented by TweenConstraintsVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDataFromXml(data)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\framework\entities\abstract\TweenManagerMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:36 Støední Evropa (letní èas)
