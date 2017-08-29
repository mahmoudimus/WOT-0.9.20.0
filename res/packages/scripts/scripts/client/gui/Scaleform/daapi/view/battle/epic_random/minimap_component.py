# 2017.08.29 21:45:56 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/epic_random/minimap_component.py
from gui.Scaleform.daapi.view.battle.classic.minimap import ClassicMinimapComponent
from gui.Scaleform.daapi.view.battle.shared.minimap import settings
from gui.Scaleform.daapi.view.battle.classic.minimap import TeamsOrControlsPointsPlugin
_SCALE_FAC = 2.0 / 3.0

class EpicRandomMinimapComponent(ClassicMinimapComponent):

    def _setupPlugins(self, arenaVisitor):
        setup = super(EpicRandomMinimapComponent, self)._setupPlugins(arenaVisitor)
        setup['points'] = EpicRandomTeamsOrControlsPointsPlugin
        return setup


class EpicRandomTeamsOrControlsPointsPlugin(TeamsOrControlsPointsPlugin):

    def _addPointEntry(self, symbol, position, number):
        entryID = super(EpicRandomTeamsOrControlsPointsPlugin, self)._addPointEntry(symbol, position, number)
        self._invoke(entryID, 'setScale', _SCALE_FAC)
        return entryID
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\battle\epic_random\minimap_component.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:45:56 Støední Evropa (letní èas)
