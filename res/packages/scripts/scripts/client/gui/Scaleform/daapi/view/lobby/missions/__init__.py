# 2017.08.29 21:47:12 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/missions/__init__.py
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import ViewSettings, GroupedViewSettings, ViewTypes, ScopeTemplates
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.Scaleform.genConsts.QUESTS_ALIASES import QUESTS_ALIASES
from gui.app_loader.settings import APP_NAME_SPACE
from gui.shared import EVENT_BUS_SCOPE

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.hangar.filter_popover import VehiclesFilterPopover
    from gui.Scaleform.daapi.view.lobby.missions.mission_details_container_view import MissionDetailsContainerView
    from gui.Scaleform.daapi.view.lobby.missions.missions_filter_popover import MissionsFilterPopoverView
    from gui.Scaleform.daapi.view.lobby.missions.missions_page import MissionsPage
    from gui.Scaleform.daapi.view.lobby.missions.missions_token_popover import MissionsTokenPopover
    from gui.Scaleform.daapi.view.lobby.missions.missions_vehicle_selector import MissionsVehicleSelector, VehicleSelectorCarousel
    from gui.Scaleform.daapi.view.lobby.missions.missions_views import MissionsMarathonsView, MissionsCategoriesView, CurrentVehicleMissionsView
    return (ViewSettings(VIEW_ALIAS.LOBBY_MISSIONS, MissionsPage, 'missionsPage.swf', ViewTypes.LOBBY_SUB, VIEW_ALIAS.LOBBY_MISSIONS, ScopeTemplates.LOBBY_SUB_SCOPE),
     ViewSettings(VIEW_ALIAS.LOBBY_MISSION_DETAILS, MissionDetailsContainerView, 'missionsDetails.swf', ViewTypes.LOBBY_TOP_SUB, VIEW_ALIAS.LOBBY_MISSION_DETAILS, ScopeTemplates.LOBBY_SUB_SCOPE, True),
     ViewSettings(QUESTS_ALIASES.MISSIONS_MARATHONS_VIEW_PY_ALIAS, MissionsMarathonsView, None, ViewTypes.COMPONENT, None, ScopeTemplates.VIEW_SCOPE),
     ViewSettings(QUESTS_ALIASES.MISSIONS_CATEGORIES_VIEW_PY_ALIAS, MissionsCategoriesView, None, ViewTypes.COMPONENT, None, ScopeTemplates.VIEW_SCOPE),
     ViewSettings(QUESTS_ALIASES.CURRENT_VEHICLE_MISSIONS_VIEW_PY_ALIAS, CurrentVehicleMissionsView, None, ViewTypes.COMPONENT, None, ScopeTemplates.VIEW_SCOPE),
     ViewSettings(QUESTS_ALIASES.MISSIONS_VEHICLE_SELECTOR_ALIAS, MissionsVehicleSelector, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(QUESTS_ALIASES.VEHICLE_SELECTOR_CAROUSEL_ALIAS, VehicleSelectorCarousel, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     GroupedViewSettings(QUESTS_ALIASES.MISSIONS_FILTER_POPOVER_ALIAS, MissionsFilterPopoverView, 'missionsFilterPopoverView.swf', ViewTypes.WINDOW, QUESTS_ALIASES.MISSIONS_FILTER_POPOVER_ALIAS, QUESTS_ALIASES.MISSIONS_FILTER_POPOVER_ALIAS, ScopeTemplates.DEFAULT_SCOPE),
     GroupedViewSettings(QUESTS_ALIASES.MISSIONS_TOKEN_POPOVER_ALIAS, MissionsTokenPopover, 'missionsTokenPopover.swf', ViewTypes.WINDOW, QUESTS_ALIASES.MISSIONS_TOKEN_POPOVER_ALIAS, QUESTS_ALIASES.MISSIONS_TOKEN_POPOVER_ALIAS, ScopeTemplates.DEFAULT_SCOPE),
     GroupedViewSettings(VIEW_ALIAS.VEHICLES_FILTER_POPOVER, VehiclesFilterPopover, 'vehiclesFiltersPopoverView.swf', ViewTypes.WINDOW, VIEW_ALIAS.VEHICLES_FILTER_POPOVER, VIEW_ALIAS.VEHICLES_FILTER_POPOVER, ScopeTemplates.DEFAULT_SCOPE))


def getBusinessHandlers():
    return (MissionsPackageBusinessHandler(),)


class MissionsPackageBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = ((QUESTS_ALIASES.MISSIONS_FILTER_POPOVER_ALIAS, self.loadViewByCtxEvent),
         (QUESTS_ALIASES.MISSIONS_TOKEN_POPOVER_ALIAS, self.loadViewByCtxEvent),
         (VIEW_ALIAS.LOBBY_MISSIONS, self.loadViewByCtxEvent),
         (VIEW_ALIAS.LOBBY_MISSION_DETAILS, self.loadViewByCtxEvent))
        super(MissionsPackageBusinessHandler, self).__init__(listeners, APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\missions\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:47:12 St�edn� Evropa (letn� �as)
