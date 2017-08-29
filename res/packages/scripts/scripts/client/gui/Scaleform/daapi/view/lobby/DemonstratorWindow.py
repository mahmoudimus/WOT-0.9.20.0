# 2017.08.29 21:46:32 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/DemonstratorWindow.py
import ArenaType
from gui.Scaleform.daapi.view.meta.DemonstratorWindowMeta import DemonstratorWindowMeta
from gui.prb_control.dispatcher import g_prbLoader
from gui.prb_control.entities.base.ctx import PrbAction
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext

class DemonstratorWindow(DemonstratorWindowMeta):
    lobbyContext = dependency.descriptor(ILobbyContext)

    def _populate(self):
        super(DemonstratorWindow, self)._populate()
        maps = dict(ctf=[], assault=[], domination=[], nations=[], ctf30x30=[], domination30x30=[])
        serverSettings = self.lobbyContext.getServerSettings()
        availableRandomMaps = serverSettings.getRandomMapsForDemonstrator()
        for arenaTypeID, arenaType in ArenaType.g_cache.iteritems():
            if arenaType.explicitRequestOnly:
                continue
            if arenaType.gameplayName not in maps:
                continue
            gameplayID, geometryID = ArenaType.parseTypeID(arenaTypeID)
            geometry = (geometryID, gameplayID)
            if any((geometry in divisionMaps for divisionMaps in availableRandomMaps.itervalues())):
                maps[arenaType.gameplayName].append({'id': arenaTypeID,
                 'name': arenaType.name,
                 'type': arenaType.gameplayName})

        sorting = lambda item: item['name']
        self.as_setDataS({'standard': sorted(maps['ctf'] + maps['ctf30x30'], key=sorting),
         'assault': sorted(maps['assault'], key=sorting),
         'encounter': sorted(maps['domination'] + maps['domination30x30'], key=sorting),
         'nations': sorted(maps['nations'], key=sorting)})

    def onMapSelected(self, mapID):
        dispatcher = g_prbLoader.getDispatcher()
        if dispatcher is not None:
            dispatcher.doAction(PrbAction(None, mapID=mapID))
            self.onWindowClose()
        return

    def onWindowClose(self):
        self.destroy()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\DemonstratorWindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:46:33 St�edn� Evropa (letn� �as)
