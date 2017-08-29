# 2017.08.29 21:52:11 Støední Evropa (letní èas)
# Embedded file name: scripts/client/web_client_api/commands/ranked_battles.py
from collections import namedtuple
from command import SchemeValidator, CommandHandler, instantiateObject
_RankedBattlesCommand = namedtuple('_RankedBattlesCommand', ('action',))
_RankedBattlesCommand.__new__.__defaults__ = (None,)
_RankedBattlesCommandScheme = {'required': (('action', basestring),)}

class RankedBattlesCommand(_RankedBattlesCommand, SchemeValidator):
    """
    Represents Ranked battles specific web command.
    """

    def __init__(self, *args, **kwargs):
        super(RankedBattlesCommand, self).__init__(_RankedBattlesCommandScheme)


def createRankedBattlesHandler(handlerFunc):
    data = {'name': 'ranked_battles',
     'cls': RankedBattlesCommand,
     'handler': handlerFunc}
    return instantiateObject(CommandHandler, data)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\web_client_api\commands\ranked_battles.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:52:11 Støední Evropa (letní èas)
