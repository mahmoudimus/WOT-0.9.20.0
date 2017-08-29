# 2017.08.29 21:45:30 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/prb_control/entities/battle_session/legacy/ctx.py
from gui.prb_control.entities.base.legacy.ctx import JoinLegacyCtx
from gui.prb_control.settings import FUNCTIONAL_FLAG
from gui.shared.utils.decorators import ReprInjector

@ReprInjector.withParent(('getID', 'prbID'), ('getPrbTypeName', 'type'), ('getWaitingID', 'waitingID'))

class JoinBattleSessionCtx(JoinLegacyCtx):
    """
    Context to join battle session mode
    """
    __slots__ = ()

    def __init__(self, prbID, prbType, waitingID = '', flags = FUNCTIONAL_FLAG.UNDEFINED):
        super(JoinBattleSessionCtx, self).__init__(prbID, prbType, waitingID=waitingID, flags=flags)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\prb_control\entities\battle_session\legacy\ctx.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:45:30 Støední Evropa (letní èas)
