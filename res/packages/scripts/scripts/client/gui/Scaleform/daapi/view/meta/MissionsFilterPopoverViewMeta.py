# 2017.08.29 21:48:16 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MissionsFilterPopoverViewMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class MissionsFilterPopoverViewMeta(SmartPopOverView):

    def changeFilter(self, hideUnavailable, hideDone):
        self._printOverrideError('changeFilter')

    def setDefaultFilter(self):
        self._printOverrideError('setDefaultFilter')

    def as_setInitDataS(self, data):
        """
        :param data: Represented by MissionsFilterPopoverInitVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_setStateS(self, data):
        """
        :param data: Represented by MissionsFilterPopoverStateVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setState(data)

    def as_enableDefaultBtnS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_enableDefaultBtn(value)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\MissionsFilterPopoverViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:16 Støední Evropa (letní èas)
