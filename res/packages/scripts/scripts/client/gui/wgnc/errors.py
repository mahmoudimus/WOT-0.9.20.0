# 2017.08.29 21:50:26 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/wgnc/errors.py


class ParseError(Exception):

    def __init__(self, *args, **kwargs):
        super(ParseError, self).__init__(*args, **kwargs)


class ValidationError(Exception):

    def __init__(self, *args, **kwargs):
        super(ValidationError, self).__init__(*args, **kwargs)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\wgnc\errors.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:50:26 St�edn� Evropa (letn� �as)
