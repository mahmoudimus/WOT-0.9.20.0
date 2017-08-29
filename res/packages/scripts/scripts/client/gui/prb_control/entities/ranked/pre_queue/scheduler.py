# 2017.08.29 21:45:37 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/prb_control/entities/ranked/pre_queue/scheduler.py
import constants
from gui import SystemMessages
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES
from gui.prb_control.entities.base.pre_queue.ctx import LeavePreQueueCtx
from gui.prb_control.entities.base.scheduler import BaseScheduler
from gui.prb_control.events_dispatcher import g_eventDispatcher
from gui.prb_control.formatters.windows import SwitchPeripheryRankedCtx
from gui.ranked_battles.constants import PRIME_TIME_STATUS
from helpers import dependency, i18n
from skeletons.gui.game_control import IRankedBattlesController

class RankedScheduler(BaseScheduler):
    rankedController = dependency.descriptor(IRankedBattlesController)

    def __init__(self, entity):
        super(RankedScheduler, self).__init__(entity)
        self.__isPrimeTime = False

    def init(self):
        status, _ = self.rankedController.getPrimeTimeStatus()
        self.__isPrimeTime = status == PRIME_TIME_STATUS.AVAILABLE
        self.rankedController.onPrimeTimeStatusUpdated += self.__update
        self.__show(isInit=True)

    def fini(self):
        self.rankedController.onPrimeTimeStatusUpdated -= self.__update

    def __update(self, status):
        """
        Process update
        :param status: Prime time status
        """
        if not self.rankedController.isAvailable():
            self._entity.leave(LeavePreQueueCtx(waitingID='prebattle/leave'))
            return
        isPrimeTime = status == PRIME_TIME_STATUS.AVAILABLE
        if isPrimeTime != self.__isPrimeTime:
            self.__isPrimeTime = isPrimeTime
            self.__show()
            g_eventDispatcher.updateUI()

    def __show(self, isInit = False):
        """
        Show UI elements: system message, window
        :param isInit: flag indicating is this method called from init()
        """
        if not self.__isPrimeTime:
            SystemMessages.pushMessage(i18n.makeString(SYSTEM_MESSAGES.RANKED_NOTIFICATION_PRIMETIME), type=SystemMessages.SM_TYPE.PrimeTime)
            if self.rankedController.hasAnyPeripheryWithPrimeTime() and not constants.IS_CHINA:
                g_eventDispatcher.showSwitchPeripheryWindow(ctx=SwitchPeripheryRankedCtx(), isModal=False)
        elif not isInit:
            SystemMessages.pushMessage(i18n.makeString(SYSTEM_MESSAGES.RANKED_NOTIFICATION_AVAILABLE), type=SystemMessages.SM_TYPE.RankedBattlesAvailable)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\ranked\pre_queue\scheduler.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:45:37 St�edn� Evropa (letn� �as)
