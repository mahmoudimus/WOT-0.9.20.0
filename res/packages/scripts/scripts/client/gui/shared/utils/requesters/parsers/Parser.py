# 2017.08.29 21:50:22 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/utils/requesters/parsers/Parser.py


class Parser(object):

    @staticmethod
    def parseVehicles(data):
        return data

    @staticmethod
    def parseModules(data, type):
        return data

    @staticmethod
    def getParser(itemTypeID):
        if itemTypeID == 1:
            return Parser.parseVehicles
        return lambda data: Parser.parseModules(data, itemTypeID)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\utils\requesters\parsers\Parser.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:50:22 Støední Evropa (letní èas)
