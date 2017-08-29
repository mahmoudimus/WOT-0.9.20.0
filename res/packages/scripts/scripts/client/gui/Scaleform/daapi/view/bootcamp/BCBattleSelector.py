# 2017.08.29 21:46:19 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCBattleSelector.py
from gui.Scaleform.daapi.view.lobby.header.BattleTypeSelectPopover import BattleTypeSelectPopover
from debug_utils import LOG_DEBUG
from gui.Scaleform.daapi.view.lobby.header import battle_selector_items
from gui.prb_control.events_dispatcher import g_eventDispatcher

class BCBattleSelector(BattleTypeSelectPopover):

    def _dispose(self):
        super(BCBattleSelector, self)._dispose()
        from bootcamp.BootcampGarage import g_bootcampGarage
        g_bootcampGarage.runViewAlias('hangar')

    def as_updateS(self, items, isShowDemonstrator, demonstratorEnabled):
        LOG_DEBUG('BCBattleSelector', items)
        for battleTypeItem in items:
            if battleTypeItem['data'] != 'random':
                battleTypeItem['disabled'] = True

        super(BCBattleSelector, self).as_updateS(items, isShowDemonstrator, demonstratorEnabled)

    def selectFight(self, actionName):
        super(BCBattleSelector, self).selectFight(actionName)
        if actionName == 'random':
            from bootcamp.BootcampGarage import g_bootcampGarage
            g_bootcampGarage.removeTutorialBattleMode()
            g_eventDispatcher.updateUI()
            g_bootcampGarage.runCustomAction('callbackOnBattleReady')
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\bootcamp\BCBattleSelector.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:46:19 Støední Evropa (letní èas)
