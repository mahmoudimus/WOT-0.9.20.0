# 2017.08.29 21:52:10 Støední Evropa (letní èas)
# Embedded file name: scripts/client/web_client_api/commands/clan_management.py
from collections import namedtuple
from command import SchemeValidator, CommandHandler, instantiateObject
_ClanManagementCommand = namedtuple('_ClanManagementCommand', ('action', 'custom_parameters'))
_ClanManagementCommand.__new__.__defaults__ = (None, {})
_ClanManagementCommandScheme = {'required': (('action', basestring),)}

class ClanManagementCommand(_ClanManagementCommand, SchemeValidator):
    """
    Represents web command for clan management.
    """

    def __init__(self, *args, **kwargs):
        super(ClanManagementCommand, self).__init__(_ClanManagementCommandScheme)


def createClanManagementHandler(handlerFunc):
    data = {'name': 'clan_management',
     'cls': ClanManagementCommand,
     'handler': handlerFunc}
    return instantiateObject(CommandHandler, data)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\web_client_api\commands\clan_management.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:52:10 Støední Evropa (letní èas)
