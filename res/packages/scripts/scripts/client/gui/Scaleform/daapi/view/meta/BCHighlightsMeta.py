# 2017.08.29 21:48:03 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BCHighlightsMeta.py
from gui.Scaleform.framework.entities.View import View

class BCHighlightsMeta(View):

    def onComponentTriggered(self, highlightId):
        self._printOverrideError('onComponentTriggered')

    def onHighlightAnimationComplete(self, highlightId):
        self._printOverrideError('onHighlightAnimationComplete')

    def as_setDescriptorsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setDescriptors(data)

    def as_addHighlightS(self, highlightId):
        if self._isDAAPIInited():
            return self.flashObject.as_addHighlight(highlightId)

    def as_removeHighlightS(self, highlightId):
        if self._isDAAPIInited():
            return self.flashObject.as_removeHighlight(highlightId)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BCHighlightsMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:03 Støední Evropa (letní èas)
