# 2017.08.29 21:44:14 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/FX/Joints/DummyModel.py
from FX import s_sectionProcessors
from FX import typeCheck
from FX.Joint import Joint
from bwdebug import *
from functools import partial
import BigWorld
import traceback

class DummyModel(Joint):
    """
    This joint attaches a PyAttachment to a dummy model.  It follows the
    player around, but can be made to follow the camera instead.  If the
    player is not available for some reason, it will follow the camera instead.
    """

    def __init__(self, followPlayer):
        self.dummy = None
        self.followPlayer = followPlayer
        if BigWorld.component == 'editor':
            self.followPlayer = False
        return

    def attach(self, actor, source, target = None):
        if actor.attached:
            ERROR_MSG('actor is already attached!', self, actor, source)
            return 0
        self._ensureDummyExists()
        try:
            self.dummy.root.attach(actor)
        except:
            ERROR_MSG('error in addModel to dummy', self, actor, source)

    def detach(self, actor, source, target = None):
        if not actor.attached:
            return
        self.dummy.root.detach(actor)
        BigWorld.delModel(self.dummy)

    def _ensureDummyExists(self):
        if None is self.dummy:
            self.dummy = BigWorld.Model('')
            self.dummy.visibleAttachments = True
            BigWorld.addModel(self.dummy)
            if self.followPlayer and BigWorld.player() != None:
                servo = BigWorld.Servo(BigWorld.player().matrix)
            else:
                servo = BigWorld.Servo(BigWorld.InvViewMatrix())
            self.dummy.motors = (servo,)
        return


s_sectionProcessors['DummyModel'] = partial(DummyModel, True)
s_sectionProcessors['Camera'] = partial(DummyModel, False)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\FX\Joints\DummyModel.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:44:14 St�edn� Evropa (letn� �as)
