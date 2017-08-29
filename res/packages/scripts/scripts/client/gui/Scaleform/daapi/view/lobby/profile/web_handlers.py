# 2017.08.29 21:47:23 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/profile/web_handlers.py
from gui.shared.event_dispatcher import showProfileWindow, requestProfile
from web_client_api.commands.window_navigator import OpenProfileCommand

def _openProfile(command):
    """
    Opens profile window
    """

    def onDossierReceived(databaseID, userName):
        showProfileWindow(databaseID, userName)

    requestProfile(command.database_id, command.user_name, successCallback=onDossierReceived)


OPEN_WINDOW_PROFILE_SUB_COMMANS = {'profile_window': (OpenProfileCommand, _openProfile)}
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\profile\web_handlers.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:47:23 Støední Evropa (letní èas)
