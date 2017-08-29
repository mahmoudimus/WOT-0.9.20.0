# 2017.08.29 21:48:15 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/LobbyMenuMeta.py
from gui.Scaleform.framework.entities.View import View

class LobbyMenuMeta(View):

    def settingsClick(self):
        self._printOverrideError('settingsClick')

    def cancelClick(self):
        self._printOverrideError('cancelClick')

    def refuseTraining(self):
        self._printOverrideError('refuseTraining')

    def logoffClick(self):
        self._printOverrideError('logoffClick')

    def quitClick(self):
        self._printOverrideError('quitClick')

    def versionInfoClick(self):
        self._printOverrideError('versionInfoClick')

    def onCounterNeedUpdate(self):
        self._printOverrideError('onCounterNeedUpdate')

    def bootcampClick(self):
        self._printOverrideError('bootcampClick')

    def onEscapePress(self):
        self._printOverrideError('onEscapePress')

    def as_setVersionMessageS(self, data):
        """
        :param data: Represented by VersionMessageVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setVersionMessage(data)

    def as_setCounterS(self, counters):
        """
        :param counters: Represented by Vector.<CountersVo> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCounter(counters)

    def as_removeCounterS(self, counters):
        """
        :param counters: Represented by Vector.<String> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_removeCounter(counters)

    def as_setBootcampButtonLabelS(self, label, icon):
        if self._isDAAPIInited():
            return self.flashObject.as_setBootcampButtonLabel(label, icon)

    def as_showBootcampButtonS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showBootcampButton(value)

    def as_setMenuStateS(self, state):
        if self._isDAAPIInited():
            return self.flashObject.as_setMenuState(state)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\LobbyMenuMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:15 Støední Evropa (letní èas)
