# 2017.08.29 21:52:08 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/Vibroeffects/Controllers/OnceController.py
from Vibroeffects import VibroManager

class OnceController:

    def __init__(self, effectName, gain = 100):
        VibroManager.g_instance.launchQuickEffect(effectName, 1, gain)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\Vibroeffects\Controllers\OnceController.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:52:08 St�edn� Evropa (letn� �as)
