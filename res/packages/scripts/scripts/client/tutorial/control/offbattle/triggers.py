# 2017.08.29 21:51:49 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/tutorial/control/offbattle/triggers.py
from constants import QUEUE_TYPE
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.prb_control.entities.listener import IGlobalListener
from tutorial.logger import LOG_ERROR
from tutorial.control.context import GlobalStorage, GLOBAL_FLAG
from tutorial.control.offbattle.context import OffBattleClientCtx
from tutorial.control.offbattle.functional import ContentChangedEvent
from tutorial.control.triggers import Trigger
__all__ = ('TutorialModeTrigger', 'TutorialQueueTrigger', 'AllBonusesTrigger')

class TutorialModeTrigger(Trigger, IGlobalListener):
    _inAvailable = GlobalStorage(GLOBAL_FLAG.MODE_IS_AVAILABLE, False)

    def __init__(self, triggerID):
        super(TutorialModeTrigger, self).__init__(triggerID)
        self._inMode = False

    def run(self):
        if not self.isSubscribed:
            self.startGlobalListening()
            self.isSubscribed = True
        self.__setState()
        super(TutorialModeTrigger, self).run()

    def isOn(self, *args):
        return self._inMode

    def clear(self):
        if self.isSubscribed:
            self.stopGlobalListening()
            self.isSubscribed = False
        self._inMode = False
        super(TutorialModeTrigger, self).clear()

    def onPrbEntitySwitched(self):
        self.__setState()
        self.toggle(isOn=self._inMode)

    def __setState(self):
        funcState = self.prbDispatcher.getFunctionalState()
        self._inMode = funcState.isInPreQueue(QUEUE_TYPE.TUTORIAL)
        self._inAvailable = funcState.isInPreQueue(QUEUE_TYPE.RANDOMS) or funcState.isInPreQueue(QUEUE_TYPE.SANDBOX)


class TutorialQueueTrigger(Trigger, IGlobalListener):
    _inQueue = GlobalStorage(GLOBAL_FLAG.IN_QUEUE, False)

    def __init__(self, triggerID, popUpID):
        super(TutorialQueueTrigger, self).__init__(triggerID)
        self._event = ContentChangedEvent(popUpID)

    def run(self):
        if not self.isSubscribed:
            self.startGlobalListening()
            self.isSubscribed = True
        super(TutorialQueueTrigger, self).run()

    def isOn(self, *args):
        return self._inQueue

    def clear(self):
        self._gui.hideWaiting('queue')
        if self.isSubscribed:
            self.stopGlobalListening()
            self.isSubscribed = False
        self._inQueue = False
        super(TutorialQueueTrigger, self).clear()

    def onEnqueued(self, queueType, *args):
        if queueType != QUEUE_TYPE.TUTORIAL:
            return
        if len(args) < 3:
            LOG_ERROR('Number of argument is invalid', args)
            queueNumber, queueLen, avgWaitingTime = (0, 0, 0)
        else:
            queueNumber, queueLen, avgWaitingTime = args[:3]
        self._event.fire(avgWaitingTime)
        if not self._inQueue:
            self._inQueue = True
            self.toggle(isOn=True)

    def onDequeued(self, queueType, *args):
        if queueType != QUEUE_TYPE.TUTORIAL:
            return
        if self._inQueue:
            self._inQueue = False
            self.toggle(isOn=False)

    def onEnqueueError(self, queueType, *args):
        if queueType == QUEUE_TYPE.TUTORIAL:
            self._tutorial.refuse()

    def onKickedFromQueue(self, queueType, *args):
        if queueType == QUEUE_TYPE.TUTORIAL:
            self._tutorial.refuse()

    def onKickedFromArena(self, queueType, *args):
        if queueType == QUEUE_TYPE.TUTORIAL:
            self._tutorial.refuse()

    def onArenaJoinFailure(self, queueType, *args):
        if queueType == QUEUE_TYPE.TUTORIAL:
            self._tutorial.refuse()


class AllBonusesTrigger(Trigger):

    def __init__(self, triggerID, setVarID):
        super(AllBonusesTrigger, self).__init__(triggerID)
        self._setVarID = setVarID
        self._battleSnap = OffBattleClientCtx.fetch(self._cache).completed
        self._statsSnap = self._bonuses.getCompleted()

    def run(self):
        self.isRunning = True
        if not self.isSubscribed:
            self.isSubscribed = True
            g_clientUpdateManager.addCallbacks({'stats.tutorialsCompleted': self.onTutorialCompleted})
        self.toggle(isOn=self.isOn(self._bonuses.getCompleted()))

    def isOn(self, completed):
        return completed & self._battleSnap == self._battleSnap

    def clear(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.isSubscribed = False
        self.isRunning = False

    def onTutorialCompleted(self, completed):
        if completed is not None:
            self._tutorial.getVars().set(self._setVarID, completed - self._statsSnap)
            self._bonuses.setCompleted(completed)
            if self.isOn(completed):
                self.toggle(isOn=True)
        return
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\tutorial\control\offbattle\triggers.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:51:49 St�edn� Evropa (letn� �as)
