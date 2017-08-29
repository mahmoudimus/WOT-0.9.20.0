# 2017.08.29 21:52:31 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/debug_utils_bootcamp.py
from debug_utils import _doLog, _LogWrapper
from debug_utils import LOG_CURRENT_EXCEPTION, LOG_TAGS, LOG_LEVEL

@_LogWrapper(LOG_LEVEL.SVR_RELEASE)
def LOG_DEBUG_BOOTCAMP(msg, *kargs, **kwargs):
    kwargs.setdefault('tags', []).append(LOG_TAGS.BOOTCAMP)
    _doLog('DEBUG', msg, kargs, kwargs)


@_LogWrapper(LOG_LEVEL.DEV)
def LOG_DEBUG_DEV_BOOTCAMP(msg, *kargs, **kwargs):
    kwargs.setdefault('tags', []).append(LOG_TAGS.BOOTCAMP)
    _doLog('DEBUG', msg, kargs, kwargs)


@_LogWrapper(LOG_LEVEL.RELEASE)
def LOG_NOTE_BOOTCAMP(msg, *kargs, **kwargs):
    kwargs.setdefault('tags', []).append(LOG_TAGS.BOOTCAMP)
    _doLog('NOTE', msg, kargs, kwargs)


@_LogWrapper(LOG_LEVEL.RELEASE)
def LOG_WARNING_BOOTCAMP(msg, *kargs, **kwargs):
    kwargs.setdefault('tags', []).append(LOG_TAGS.BOOTCAMP)
    _doLog('WARNING', msg, kargs, kwargs)


@_LogWrapper(LOG_LEVEL.RELEASE)
def LOG_ERROR_BOOTCAMP(msg, *kargs, **kwargs):
    kwargs.setdefault('tags', []).append(LOG_TAGS.BOOTCAMP)
    _doLog('ERROR', msg, kargs, kwargs)


@_LogWrapper(LOG_LEVEL.RELEASE)
def LOG_CODEPOINT_WARNING_BOOTCAMP(*kargs, **kwargs):
    kwargs.setdefault('tags', []).append(LOG_TAGS.BOOTCAMP)
    _doLog('WARNING', 'this code point should have never been reached', kargs, kwargs)


def LOG_CURRENT_EXCEPTION_BOOTCAMP():
    LOG_CURRENT_EXCEPTION(tags=[LOG_TAGS.BOOTCAMP], frame=2)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\debug_utils_bootcamp.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:52:31 St�edn� Evropa (letn� �as)
