# 2017.08.29 21:47:07 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hof/web_handlers.py
from functools import partial
from gui.Scaleform.daapi.view.lobby.clans.web_handlers import OPEN_WINDOW_CLAN_SUB_COMMANDS
from gui.Scaleform.daapi.view.lobby.shared.web_handlers import handleVehiclesCommand, createOpenWindowCommandHandler, handleSoundCommand, handleRequestCommand, handleContextMenuCommand, handleOpenTabCommand, handleCloseWindowCommand
from web_client_api.commands import createVehiclesHandler, createOpenWindowHandler, createSoundHandler, createRequestHandler, createContextMenuHandler, createOpenTabHandler, createCloseWindowHandler

def createHofWebHandlers():
    handlers = [createVehiclesHandler(handleVehiclesCommand),
     createOpenWindowHandler(createOpenWindowCommandHandler(OPEN_WINDOW_CLAN_SUB_COMMANDS)),
     createSoundHandler(handleSoundCommand),
     createRequestHandler(handleRequestCommand),
     createContextMenuHandler(handleContextMenuCommand),
     createOpenTabHandler(handleOpenTabCommand),
     createCloseWindowHandler(partial(handleCloseWindowCommand, None, isWindow=False))]
    return handlers
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\hof\web_handlers.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:47:07 Støední Evropa (letní èas)
