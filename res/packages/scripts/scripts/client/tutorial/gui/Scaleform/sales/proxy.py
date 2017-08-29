# 2017.08.29 21:52:02 Støední Evropa (letní èas)
# Embedded file name: scripts/client/tutorial/gui/Scaleform/sales/proxy.py
from tutorial.gui import GUI_EFFECT_NAME
from tutorial.gui.Scaleform import effects_player
from tutorial.gui.Scaleform.lobby.proxy import SfLobbyProxy

class SfSalesProxy(SfLobbyProxy):

    def __init__(self):
        effects = {GUI_EFFECT_NAME.SHOW_HINT: effects_player.ShowChainHint(),
         GUI_EFFECT_NAME.SET_CRITERIA: effects_player.SetCriteriaEffect(),
         GUI_EFFECT_NAME.SET_TRIGGER: effects_player.SetTriggerEffect()}
        super(SfSalesProxy, self).__init__(effects_player.EffectsPlayer(effects))

    def fini(self):
        super(SfSalesProxy, self).fini()

    def getViewSettings(self):
        return {}

    def getViewsAliases(self):
        return {}
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\tutorial\gui\Scaleform\sales\proxy.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:52:02 Støední Evropa (letní èas)
