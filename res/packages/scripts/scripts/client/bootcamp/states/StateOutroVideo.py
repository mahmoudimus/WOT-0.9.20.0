# 2017.08.29 21:43:56 Støední Evropa (letní èas)
# Embedded file name: scripts/client/bootcamp/states/StateOutroVideo.py
from AbstractState import AbstractState
from bootcamp.states import STATE
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.shared import EVENT_BUS_SCOPE
from gui.shared import events
from gui.shared import g_eventBus

class StateOutroVideo(AbstractState):

    def __init__(self):
        super(StateOutroVideo, self).__init__(STATE.OUTRO_VIDEO)

    def handleKeyEvent(self, event):
        pass

    def _doActivate(self):
        g_eventBus.handleEvent(events.LoadViewEvent(VIEW_ALIAS.BOOTCAMP_OUTRO_VIDEO, None, {'video': 'video/_bootcampFinish.usm'}), EVENT_BUS_SCOPE.LOBBY)
        return

    def _doDeactivate(self):
        pass
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\bootcamp\states\StateOutroVideo.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:43:56 Støední Evropa (letní èas)
