# 2017.08.29 21:52:11 Støední Evropa (letní èas)
# Embedded file name: scripts/client/web_client_api/commands/request.py
from collections import namedtuple
from command import SchemeValidator, CommandHandler, instantiateObject
_RequestCommand = namedtuple('_RequestCommand', ('request_id',))
_RequestCommand.__new__.__defaults__ = (None,)
_RequestCommandScheme = {'required': (('request_id', basestring),)}

class RequestCommand(_RequestCommand, SchemeValidator):
    """
    Represents web command for general purpose requests (eg. Token1 and other common data).
    If there is a need to do some module-specific requests (eg. ClanManagement) then another command should be created.
    """

    def __init__(self, *args, **kwargs):
        super(RequestCommand, self).__init__(_RequestCommandScheme)


def createRequestHandler(handlerFunc):
    data = {'name': 'request',
     'cls': RequestCommand,
     'handler': handlerFunc}
    return instantiateObject(CommandHandler, data)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\web_client_api\commands\request.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:52:11 Støední Evropa (letní èas)
