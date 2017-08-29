# 2017.08.29 21:46:57 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/fortifications/__init__.py
from gui.shared import EVENT_BUS_SCOPE
from gui.app_loader.settings import APP_NAME_SPACE
from gui.prb_control.settings import FUNCTIONAL_FLAG
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.Scaleform.framework import ScopeTemplates
from gui.Scaleform.framework import ViewSettings, GroupedViewSettings, ViewTypes
from gui.Scaleform.genConsts.FORTIFICATION_ALIASES import FORTIFICATION_ALIASES

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.fortifications.components.StrongholdBattlesListView import StrongholdBattlesListView
    from gui.Scaleform.daapi.view.lobby.fortifications.StrongholdBattleRoom import StrongholdBattleRoom
    from gui.Scaleform.daapi.view.lobby.fortifications.StrongholdBattleRoomWindow import StrongholdBattleRoomWindow
    from gui.Scaleform.daapi.view.lobby.fortifications.FortReserveSelectPopover import FortReserveSelectPopover
    from gui.Scaleform.daapi.view.lobby.fortifications.StrongholdSendInvitesWindow import StrongholdSendInvitesWindow
    return (GroupedViewSettings(FORTIFICATION_ALIASES.STRONGHOLD_SEND_INVITES_WINDOW_PY, StrongholdSendInvitesWindow, 'sendInvitesWindow.swf', ViewTypes.WINDOW, '', FORTIFICATION_ALIASES.STRONGHOLD_SEND_INVITES_WINDOW_PY, ScopeTemplates.DEFAULT_SCOPE, True),
     GroupedViewSettings(FORTIFICATION_ALIASES.FORT_RESERVE_SELECT_POPOVER_ALIAS, FortReserveSelectPopover, FORTIFICATION_ALIASES.FORT_FITTING_SELECT_POPOVER_UI, ViewTypes.WINDOW, FORTIFICATION_ALIASES.FORT_RESERVE_SELECT_POPOVER_ALIAS, FORTIFICATION_ALIASES.FORT_RESERVE_SELECT_POPOVER_ALIAS, ScopeTemplates.DEFAULT_SCOPE),
     GroupedViewSettings(FORTIFICATION_ALIASES.STRONGHOLD_BATTLE_ROOM_WINDOW_ALIAS, StrongholdBattleRoomWindow, FORTIFICATION_ALIASES.FORT_BATTLE_ROOM_WINDOW_UI, ViewTypes.WINDOW, '', FORTIFICATION_ALIASES.STRONGHOLD_BATTLE_ROOM_WINDOW_ALIAS, ScopeTemplates.DEFAULT_SCOPE, True),
     ViewSettings(FORTIFICATION_ALIASES.STRONGHOLD_BATTLE_ROOM_LIST_VIEW_PY, StrongholdBattlesListView, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(FORTIFICATION_ALIASES.STRONGHOLD_BATTLE_ROOM_VIEW_PY, StrongholdBattleRoom, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE))


def getBusinessHandlers():
    return (_FortsBusinessHandler(),)


class _FortsBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = ((FORTIFICATION_ALIASES.STRONGHOLD_BATTLE_ROOM_WINDOW_ALIAS, self.__showStrongholdBattleRoomWindow), (FORTIFICATION_ALIASES.FORT_RESERVE_SELECT_POPOVER_ALIAS, self.loadViewByCtxEvent), (FORTIFICATION_ALIASES.STRONGHOLD_SEND_INVITES_WINDOW_PY, self.__showPrebattleWindow))
        super(_FortsBusinessHandler, self).__init__(listeners, APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)

    def __showStrongholdBattleRoomWindow(self, event):
        alias = name = FORTIFICATION_ALIASES.STRONGHOLD_BATTLE_ROOM_WINDOW_ALIAS
        window = self.findViewByAlias(ViewTypes.WINDOW, alias)
        if window is not None:
            if event.ctx.get('modeFlags') == FUNCTIONAL_FLAG.UNIT_BROWSER:
                window.onBrowseRallies()
        self.loadViewWithDefName(alias, name, event.ctx)
        return

    def __showPrebattleWindow(self, event):
        alias = name = event.eventType
        self.loadViewWithDefName(alias, name, event.ctx)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\fortifications\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:46:57 St�edn� Evropa (letn� �as)
