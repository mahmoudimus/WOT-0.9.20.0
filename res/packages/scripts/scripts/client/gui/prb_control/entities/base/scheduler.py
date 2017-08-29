# 2017.08.29 21:45:22 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/prb_control/entities/base/scheduler.py
import weakref
from gui.shared.utils.scheduled_notifications import Notifiable

class BaseScheduler(Notifiable):
    """
    Class that process schedules for prebattle functionality
    """

    def __init__(self, entity):
        super(BaseScheduler, self).__init__()
        self._entity = weakref.proxy(entity)

    def init(self):
        """
        Initialization method
        """
        pass

    def fini(self):
        """
        Finalization method
        """
        pass
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\base\scheduler.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:45:22 Støední Evropa (letní èas)
