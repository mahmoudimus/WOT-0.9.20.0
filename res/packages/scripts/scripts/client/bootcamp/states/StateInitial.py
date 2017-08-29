# 2017.08.29 21:43:56 Støední Evropa (letní èas)
# Embedded file name: scripts/client/bootcamp/states/StateInitial.py
from bootcamp.states import STATE
from bootcamp.states.AbstractState import AbstractState

class StateInitial(AbstractState):

    def __init__(self):
        super(StateInitial, self).__init__(STATE.INITIAL)

    def handleKeyEvent(self, event):
        pass

    def _doActivate(self):
        pass

    def _doDeactivate(self):
        pass
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\bootcamp\states\StateInitial.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:43:56 Støední Evropa (letní èas)
