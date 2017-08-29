# 2017.08.29 21:48:35 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/PopoverManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class PopoverManagerMeta(BaseDAAPIComponent):

    def requestShowPopover(self, alias, data):
        self._printOverrideError('requestShowPopover')

    def requestHidePopover(self):
        self._printOverrideError('requestHidePopover')

    def as_onPopoverDestroyS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_onPopoverDestroy()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\framework\entities\abstract\PopoverManagerMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:35 Støední Evropa (letní èas)
