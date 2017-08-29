# 2017.08.29 21:45:04 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/game_control/links.py
import re
from gui import macroses
from debug_utils import LOG_ERROR
from adisp import process, async

class URLMarcos(object):
    __MACROS_PREFIX = '$'

    def __init__(self):
        """
        Class of parser that replace macros to required value.
        """
        super(URLMarcos, self).__init__()
        self.__asyncMacroses = macroses.getAsyncMacroses()
        self.__syncMacroses = macroses.getSyncMacroses()
        macrosKeys = self.__syncMacroses.keys()
        macrosKeys.extend(self.__asyncMacroses.keys())
        patterns = []
        for macro in macrosKeys:
            patterns.append('\\%(macro)s\\(.*\\)|\\%(macro)s' % {'macro': self._getUserMacrosName(macro)})

        self.__filter = re.compile('|'.join(patterns))
        self.__argsFilter = re.compile('\\$(\\w*)(\\((.*)\\))?')

    def clear(self):
        self.__asyncMacroses = None
        self.__syncMacroses = None
        self.__argsFilter = None
        self.__filter = None
        return

    def hasMarcos(self, url):
        """
        Does url have macros.
        @return: bool.
        """
        return len(self.__filter.findall(url)) > 0

    @async
    @process
    def parse(self, url, params = None, callback = lambda *args: None):
        """
        Finds macros and replace to required value.
        @return: string containing parsed url.
        """
        for macros in self.__filter.findall(url):
            macroName, _, args = self.__argsFilter.match(macros).groups()
            replacement = yield self._replace(macroName, args, params)
            url = url.replace(macros, replacement)

        callback(url)

    @async
    @process
    def _replace(self, macros, args, params, callback):
        result = ''
        if macros in self.__asyncMacroses:
            result = yield self.__asyncMacroses[macros](self, args, params)
        elif macros in self.__syncMacroses:
            result = self.__syncMacroses[macros](args)
        else:
            LOG_ERROR('URL macros is not found', macros)
        callback(result)

    def _getUserMacrosName(self, macros):
        return '%s%s' % (self.__MACROS_PREFIX, str(macros))
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\game_control\links.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:45:04 St�edn� Evropa (letn� �as)
