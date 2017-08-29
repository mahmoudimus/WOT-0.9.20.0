# 2017.08.29 21:43:53 Støední Evropa (letní èas)
# Embedded file name: scripts/client/bootcamp/scenery/TriggerListener.py
import TriggersManager

class TriggerListener(TriggersManager.ITriggerListener):

    def __init__(self, mission):
        super(TriggerListener, self).__init__()
        self._mission = mission
        TriggersManager.g_manager.addListener(self)

    def destroy(self):
        self._mission = None
        TriggersManager.g_manager.delListener(self)
        return

    def onTriggerActivated(self, params):
        self._mission.onTriggerActivated(params)

    def onTriggerDeactivated(self, params):
        self._mission.onTriggerDeactivated(params)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\bootcamp\scenery\TriggerListener.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:43:53 Støední Evropa (letní èas)
