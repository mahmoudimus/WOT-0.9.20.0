# 2017.08.29 21:48:25 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StoreActionsViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class StoreActionsViewMeta(BaseDAAPIComponent):

    def actionSelect(self, triggerChainID):
        self._printOverrideError('actionSelect')

    def onBattleTaskSelect(self, actionId):
        self._printOverrideError('onBattleTaskSelect')

    def onActionSeen(self, actionId):
        self._printOverrideError('onActionSeen')

    def as_setDataS(self, storeActionsData):
        """
        :param storeActionsData: Represented by StoreActionsViewVo (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(storeActionsData)

    def as_actionTimeUpdateS(self, actionsTime):
        """
        :param actionsTime: Represented by Vector.<StoreActionTimeVo> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_actionTimeUpdate(actionsTime)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\StoreActionsViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:25 Støední Evropa (letní èas)
