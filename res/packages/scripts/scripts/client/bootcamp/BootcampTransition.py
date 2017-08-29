# 2017.08.29 21:43:48 Støední Evropa (letní èas)
# Embedded file name: scripts/client/bootcamp/BootcampTransition.py
from StartBootcampTransition import StartBootcampTransition
from debug_utils_bootcamp import LOG_DEBUG_DEV_BOOTCAMP

class BootcampTransition(object):
    _transitionWindow = None

    @classmethod
    def start(cls, name = 'bootcampTransitionsApp.swf'):
        if cls._transitionWindow:
            cls._transitionWindow.close()
            cls._transitionWindow = None
        cls._transitionWindow = StartBootcampTransition(name)
        cls._transitionWindow.active(True)
        return

    @classmethod
    def stop(cls):
        LOG_DEBUG_DEV_BOOTCAMP('TRANSITION_end', cls)
        if cls._transitionWindow:
            cls._transitionWindow.active(False)
            cls._transitionWindow.close()
            cls._transitionWindow = None
        return
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\bootcamp\BootcampTransition.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:43:48 Støední Evropa (letní èas)
