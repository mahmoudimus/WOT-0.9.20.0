# 2017.08.29 21:43:46 Støední Evropa (letní èas)
# Embedded file name: scripts/client/bootcamp/BootcampHooks.py


class BCClassHook0:

    def __init__(self, hookObject, hookMethodName, callback):
        hookedFunction = getattr(hookObject, hookMethodName)
        self.__hookedFunction = hookedFunction
        self.__callback = callback
        self.__hookedObject = hookObject
        self.__methodName = hookMethodName
        setattr(hookObject, hookMethodName, self.__onHook)

    def dispose(self):
        if getattr(self.__hookedObject, self.__methodName) == self.__onHook:
            setattr(self.__hookedObject, self.__methodName, self.__hookedFunction)
        self.__hookedObject = None
        self.__hookedFunction = None
        self.__callback = None
        return

    def __onHook(self):
        self.__callback()

    def callOriginal(self):
        self.__hookedFunction()

    def callOriginalInstance(self, instance):
        self.__hookedFunction(instance)


class BCClassHook1:

    def __init__(self, hookObject, hookMethodName, callback):
        hookedFunction = getattr(hookObject, hookMethodName)
        self.__hookedFunction = hookedFunction
        self.__callback = callback
        self.__hookedObject = hookObject
        self.__methodName = hookMethodName
        setattr(hookObject, hookMethodName, self.__onHook)

    def dispose(self):
        if getattr(self.__hookedObject, self.__methodName) == self.__onHook:
            setattr(self.__hookedObject, self.__methodName, self.__hookedFunction)
        self.__hookedObject = None
        self.__hookedFunction = None
        self.__callback = None
        return

    def __onHook(self, value0):
        self.__callback(value0)

    def callOriginalInstance(self, instance, value0):
        self.__hookedFunction(instance, value0)

    def callOriginal(self, value0):
        self.__hookedFunction(value0)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\bootcamp\BootcampHooks.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:43:46 Støední Evropa (letní èas)
