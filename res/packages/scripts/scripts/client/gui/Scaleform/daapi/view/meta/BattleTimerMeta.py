# 2017.08.29 21:48:02 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattleTimerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleTimerMeta(BaseDAAPIComponent):

    def as_setTotalTimeS(self, minutes, seconds):
        if self._isDAAPIInited():
            return self.flashObject.as_setTotalTime(minutes, seconds)

    def as_setColorS(self, criticalColor):
        if self._isDAAPIInited():
            return self.flashObject.as_setColor(criticalColor)

    def as_showBattleTimerS(self, show):
        if self._isDAAPIInited():
            return self.flashObject.as_showBattleTimer(show)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\BattleTimerMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:02 St�edn� Evropa (letn� �as)
