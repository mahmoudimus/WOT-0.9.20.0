# 2017.08.29 21:47:59 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AcousticPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class AcousticPopoverMeta(SmartPopOverView):

    def onActionStart(self, actionID):
        self._printOverrideError('onActionStart')

    def onSpeakerClick(self, speakerID):
        self._printOverrideError('onSpeakerClick')

    def as_setDataS(self, data):
        """
        :param data: Represented by AcousticPopoverVo (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_onItemPlayS(self, itemsID):
        """
        :param itemsID: Represented by Array (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_onItemPlay(itemsID)

    def as_onItemSelectS(self, itemsID):
        """
        :param itemsID: Represented by Array (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_onItemSelect(itemsID)

    def as_setEnableS(self, isEnable):
        if self._isDAAPIInited():
            return self.flashObject.as_setEnable(isEnable)

    def as_updateBtnEnabledS(self, btnId, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_updateBtnEnabled(btnId, isEnabled)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\AcousticPopoverMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:47:59 Støední Evropa (letní èas)
