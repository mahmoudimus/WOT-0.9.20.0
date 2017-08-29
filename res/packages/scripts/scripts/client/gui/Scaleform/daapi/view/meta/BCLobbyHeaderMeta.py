# 2017.08.29 21:48:04 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BCLobbyHeaderMeta.py
from gui.Scaleform.daapi.view.lobby.header.LobbyHeader import LobbyHeader

class BCLobbyHeaderMeta(LobbyHeader):

    def BCLobbyViewMeta(self, ctx):
        self._printOverrideError('BCLobbyViewMeta')

    def startBattle(self):
        self._printOverrideError('startBattle')

    def as_doEnableNavigationS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_doEnableNavigation()

    def as_showAnimatedS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showAnimated(data)

    def as_setHeaderButtonsS(self, data):
        """
        :param data: Represented by Array (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderButtons(data)

    def as_setHeaderKeysMapS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderKeysMap(data)

    def as_setMainMenuKeysMapS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setMainMenuKeysMap(data)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BCLobbyHeaderMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:04 Støední Evropa (letní èas)
