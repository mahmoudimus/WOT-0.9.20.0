# 2017.08.29 21:46:23 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCRibbonsPanel.py
from gui.Scaleform.daapi.view.battle.shared.ribbons_panel import BattleRibbonsPanel
from bootcamp.Bootcamp import g_bootcamp

class BCRibbonsPanel(BattleRibbonsPanel):

    def __init__(self):
        super(BCRibbonsPanel, self).__init__()
        self._ribbonsSettings = None
        return

    def _populate(self):
        super(BCRibbonsPanel, self)._populate()
        self._ribbonsSettings = g_bootcamp.getBattleRibbonsSettings()

    def _shouldShowRibbon(self, ribbon):
        ribbonName = ribbon.getType()
        if ribbonName in self._ribbonsSettings:
            return super(BCRibbonsPanel, self)._shouldShowRibbon(ribbon)
        else:
            return False

    def _dispose(self):
        super(BCRibbonsPanel, self)._dispose()
        self._ribbonsSettings = None
        return
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\bootcamp\BCRibbonsPanel.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:46:23 Støední Evropa (letní èas)
