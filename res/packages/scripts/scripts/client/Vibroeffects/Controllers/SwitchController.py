# 2017.08.29 21:52:09 Støední Evropa (letní èas)
# Embedded file name: scripts/client/Vibroeffects/Controllers/SwitchController.py
from Vibroeffects import VibroManager

class SwitchController:

    def __init__(self, effectName):
        self.__effect = VibroManager.g_instance.getEffect(effectName)

    def destroy(self):
        VibroManager.g_instance.stopEffect(self.__effect)
        self.__effect = None
        return

    def switch(self, turnOn):
        if turnOn:
            VibroManager.g_instance.startEffect(self.__effect)
        else:
            VibroManager.g_instance.stopEffect(self.__effect)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\Vibroeffects\Controllers\SwitchController.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:52:09 Støední Evropa (letní èas)
