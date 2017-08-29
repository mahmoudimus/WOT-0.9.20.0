# 2017.08.29 21:51:14 Støední Evropa (letní èas)
# Embedded file name: scripts/client/messenger/proto/migration/MigrationServerSettings.py
from messenger.proto.interfaces import IProtoSettings

class MigrationServerSettings(IProtoSettings):

    def __init__(self):
        super(MigrationServerSettings, self).__init__()

    def isEnabled(self):
        return True
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\messenger\proto\migration\MigrationServerSettings.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:51:14 Støední Evropa (letní èas)
