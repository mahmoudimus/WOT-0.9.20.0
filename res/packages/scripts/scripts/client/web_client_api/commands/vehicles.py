# 2017.08.29 21:52:11 Støední Evropa (letní èas)
# Embedded file name: scripts/client/web_client_api/commands/vehicles.py
from collections import namedtuple
from command import SchemeValidator, CommandHandler, instantiateObject
_VehiclesCommand = namedtuple('_VehiclesCommand', ('action', 'vehicle_id'))
_VehiclesCommand.__new__.__defaults__ = (None, None)
_VehiclesCommandScheme = {'required': (('action', basestring),),
 'optional': (('vehicle_id', (int, long)),)}

class VehiclesCommand(_VehiclesCommand, SchemeValidator):
    """
    Represents web command for vehicles encyclopedia.
    """

    def __init__(self, *args, **kwargs):
        super(VehiclesCommand, self).__init__(_VehiclesCommandScheme)


def createVehiclesHandler(handlerFunc):
    data = {'name': 'vehicles',
     'cls': VehiclesCommand,
     'handler': handlerFunc}
    return instantiateObject(CommandHandler, data)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\web_client_api\commands\vehicles.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:52:11 Støední Evropa (letní èas)
