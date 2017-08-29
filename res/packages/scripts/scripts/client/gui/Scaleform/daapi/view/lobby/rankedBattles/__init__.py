# 2017.08.29 21:47:31 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/rankedBattles/__init__.py
from gui.Scaleform.framework import ScopeTemplates, GroupedViewSettings
from gui.Scaleform.framework import ViewSettings, ViewTypes
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES
from gui.app_loader.settings import APP_NAME_SPACE
from gui.shared import EVENT_BUS_SCOPE

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.rankedBattles.RankedBattlesView import RankedBattlesView
    from gui.Scaleform.daapi.view.lobby.rankedBattles.RankedBattlesWelcomeView import RankedBattlesWelcomeView
    from gui.Scaleform.daapi.view.lobby.rankedBattles.RankedBattlesCyclesView import RankedBattlesCyclesView
    from gui.Scaleform.daapi.view.lobby.rankedBattles.RankedBattlesCalendarPopover import RankedBattlesCalendarPopover
    from gui.Scaleform.daapi.view.lobby.rankedBattles.RankedBattlesBattleResults import RankedBattlesBattleResults
    from gui.Scaleform.daapi.view.lobby.rankedBattles.RankedBattlesAwardsView import RankedBattlesAwardsView
    from gui.Scaleform.daapi.view.lobby.rankedBattles.RankedBattlesBrowserView import RankedBattlesBrowserView
    from gui.Scaleform.daapi.view.lobby.hangar.ranked_battles_widget import RankedBattleResultsWidget
    from gui.Scaleform.daapi.view.lobby.hangar.ranked_battles_widget import RankedBattleResultsFinalWidget
    from gui.Scaleform.daapi.view.lobby.rankedBattles.RankedBattlesSeasonCompleteView import RankedBattlesSeasonCompleteView
    from gui.Scaleform.daapi.view.lobby.rankedBattles.RankedBattlesStageCompleteView import RankedBattlesStageCompleteView
    from gui.Scaleform.daapi.view.lobby.rankedBattles.ranked_battles_prime_time_view import RankedBattlesPrimeTimeView
    return (GroupedViewSettings(RANKEDBATTLES_ALIASES.RANKED_BATTLES_CALENDAR_POPOVER, RankedBattlesCalendarPopover, RANKEDBATTLES_ALIASES.RANKED_BATTLES_CALENDAR_POPOVER_UI, ViewTypes.WINDOW, RANKEDBATTLES_ALIASES.RANKED_BATTLES_CALENDAR_POPOVER, RANKEDBATTLES_ALIASES.RANKED_BATTLES_CALENDAR_POPOVER, ScopeTemplates.LOBBY_SUB_SCOPE),
     ViewSettings(RANKEDBATTLES_ALIASES.RANKED_BATTLES_VIEW_ALIAS, RankedBattlesView, RANKEDBATTLES_ALIASES.RANKED_BATTLES_VIEW_UI, ViewTypes.LOBBY_SUB, RANKEDBATTLES_ALIASES.RANKED_BATTLES_VIEW_ALIAS, ScopeTemplates.LOBBY_SUB_SCOPE, True),
     ViewSettings(RANKEDBATTLES_ALIASES.RANKED_BATTLES_BROWSER_VIEW, RankedBattlesBrowserView, RANKEDBATTLES_ALIASES.RANKED_BATTLES_BROWSER_VIEW_UI, ViewTypes.LOBBY_SUB, RANKEDBATTLES_ALIASES.RANKED_BATTLES_BROWSER_VIEW, ScopeTemplates.LOBBY_SUB_SCOPE, True),
     ViewSettings(RANKEDBATTLES_ALIASES.RANKED_BATTLES_WELCOME_VIEW_ALIAS, RankedBattlesWelcomeView, RANKEDBATTLES_ALIASES.RANKED_BATTLES_WELCOME_VIEW_UI, ViewTypes.LOBBY_SUB, RANKEDBATTLES_ALIASES.RANKED_BATTLES_WELCOME_VIEW_ALIAS, ScopeTemplates.LOBBY_SUB_SCOPE, True),
     ViewSettings(RANKEDBATTLES_ALIASES.RANKED_BATTLES_CYCLES_VIEW_ALIAS, RankedBattlesCyclesView, RANKEDBATTLES_ALIASES.RANKED_BATTLES_CYCLES_VIEW_UI, ViewTypes.LOBBY_SUB, RANKEDBATTLES_ALIASES.RANKED_BATTLES_CYCLES_VIEW_ALIAS, ScopeTemplates.LOBBY_SUB_SCOPE, True),
     ViewSettings(RANKEDBATTLES_ALIASES.RANKED_BATTLES_BATTLE_RESULTS, RankedBattlesBattleResults, RANKEDBATTLES_ALIASES.RANKED_BATTLES_BATTLE_RESULTS_UI, ViewTypes.OVERLAY, RANKEDBATTLES_ALIASES.RANKED_BATTLES_BATTLE_RESULTS, ScopeTemplates.LOBBY_TOP_SUB_SCOPE, True),
     ViewSettings(RANKEDBATTLES_ALIASES.RANKED_BATTLES_AWARD, RankedBattlesAwardsView, RANKEDBATTLES_ALIASES.RANKED_BATTLES_AWARD_UI, ViewTypes.OVERLAY, RANKEDBATTLES_ALIASES.RANKED_BATTLES_AWARD, ScopeTemplates.LOBBY_TOP_SUB_SCOPE, True),
     ViewSettings(RANKEDBATTLES_ALIASES.RANKED_BATTLES_SEASON_COMPLETE, RankedBattlesSeasonCompleteView, RANKEDBATTLES_ALIASES.RANKED_BATTLES_SEASON_COMPLETE_UI, ViewTypes.OVERLAY, RANKEDBATTLES_ALIASES.RANKED_BATTLES_SEASON_COMPLETE, ScopeTemplates.LOBBY_TOP_SUB_SCOPE, True),
     ViewSettings(RANKEDBATTLES_ALIASES.RANKED_BATTLES_STAGE_COMPLETE, RankedBattlesStageCompleteView, RANKEDBATTLES_ALIASES.RANKED_BATTLES_STAGE_COMPLETE_UI, ViewTypes.OVERLAY, RANKEDBATTLES_ALIASES.RANKED_BATTLES_STAGE_COMPLETE, ScopeTemplates.LOBBY_TOP_SUB_SCOPE, True),
     ViewSettings(RANKEDBATTLES_ALIASES.RANKED_BATTLE_RESULTS_WIDGET, RankedBattleResultsWidget, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(RANKEDBATTLES_ALIASES.RANKED_BATTLE_RESULTS_FINAL_WIDGET, RankedBattleResultsFinalWidget, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(RANKEDBATTLES_ALIASES.RANKED_BATTLE_PRIME_TIME, RankedBattlesPrimeTimeView, RANKEDBATTLES_ALIASES.RANKED_BATTLE_PRIME_TIME_UI, ViewTypes.LOBBY_SUB, RANKEDBATTLES_ALIASES.RANKED_BATTLE_PRIME_TIME, ScopeTemplates.LOBBY_TOP_SUB_SCOPE, True))


def getBusinessHandlers():
    return (RankedBattlesPackageBusinessHandler(),)


class RankedBattlesPackageBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = ((RANKEDBATTLES_ALIASES.RANKED_BATTLES_CALENDAR_POPOVER, self.loadViewByCtxEvent),
         (RANKEDBATTLES_ALIASES.RANKED_BATTLES_VIEW_ALIAS, self.loadViewByCtxEvent),
         (RANKEDBATTLES_ALIASES.RANKED_BATTLES_BROWSER_VIEW, self.loadViewByCtxEvent),
         (RANKEDBATTLES_ALIASES.RANKED_BATTLES_WELCOME_VIEW_ALIAS, self.loadViewByCtxEvent),
         (RANKEDBATTLES_ALIASES.RANKED_BATTLES_CYCLES_VIEW_ALIAS, self.loadViewByCtxEvent),
         (RANKEDBATTLES_ALIASES.RANKED_BATTLES_BATTLE_RESULTS, self.loadViewByCtxEvent),
         (RANKEDBATTLES_ALIASES.RANKED_BATTLES_AWARD, self.loadViewByCtxEvent),
         (RANKEDBATTLES_ALIASES.RANKED_BATTLES_SEASON_COMPLETE, self.loadViewByCtxEvent),
         (RANKEDBATTLES_ALIASES.RANKED_BATTLES_STAGE_COMPLETE, self.loadViewByCtxEvent),
         (RANKEDBATTLES_ALIASES.RANKED_BATTLE_PRIME_TIME, self.loadViewByCtxEvent))
        super(RankedBattlesPackageBusinessHandler, self).__init__(listeners, APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\rankedBattles\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:47:31 St�edn� Evropa (letn� �as)
