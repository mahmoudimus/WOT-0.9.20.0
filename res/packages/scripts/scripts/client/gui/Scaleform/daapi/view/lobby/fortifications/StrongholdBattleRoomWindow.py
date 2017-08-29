# 2017.08.29 21:46:56 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/fortifications/StrongholdBattleRoomWindow.py
from constants import PREBATTLE_TYPE
from debug_utils import LOG_ERROR, LOG_DEBUG
from helpers import time_utils
from gui.Scaleform.daapi.view.meta.FortBattleRoomWindowMeta import FortBattleRoomWindowMeta
from gui.Scaleform.genConsts.CYBER_SPORT_ALIASES import CYBER_SPORT_ALIASES
from gui.Scaleform.genConsts.FORTIFICATION_ALIASES import FORTIFICATION_ALIASES
from gui.Scaleform.managers.windows_stored_data import stored_window, DATA_TYPE, TARGET_ID
from gui.prb_control import settings, prbPeripheriesHandlerProperty
from gui.prb_control.events_dispatcher import g_eventDispatcher
from gui.prb_control.formatters import messages
from gui.prb_control.entities.base.unit.listener import IStrongholdListener
from gui.prb_control.settings import SELECTOR_BATTLE_TYPES
from gui.shared import events
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.shared.utils import SelectorBattleTypesUtils as selectorUtils
from helpers import i18n
from gui.prb_control.entities.base.unit.ctx import AutoSearchUnitCtx, DeclineSearchUnitCtx, BattleQueueUnitCtx
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.shared.formatters import icons, text_styles
from gui.clans import formatters as clans_fmts
from gui.Scaleform.locale.FORTIFICATIONS import FORTIFICATIONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.Scaleform.locale.CYBERSPORT import CYBERSPORT
from gui.Scaleform.daapi.view.lobby.fortifications.StrongholdBattleRoom import StrongholdBattleRoom

@stored_window(DATA_TYPE.UNIQUE_WINDOW, TARGET_ID.CHANNEL_CAROUSEL)

class StrongholdBattleRoomWindow(FortBattleRoomWindowMeta, IStrongholdListener):

    def __init__(self, ctx = None):
        super(StrongholdBattleRoomWindow, self).__init__()
        self.__isOnMatchmakingTimerChangedRegistered = False
        self.__autosearchTimer = None
        self.currentState = ''
        return

    @prbPeripheriesHandlerProperty
    def prbPeripheriesHandler(self):
        return None

    def onWindowMinimize(self):
        g_eventDispatcher.showUnitProgressInCarousel(self.getPrbType())
        self.destroy()

    def getBrowserViewAlias(self, prbType):
        return FORTIFICATION_ALIASES.STRONGHOLD_BATTLE_ROOM_LIST_VIEW_UI

    def getRoomViewAlias(self, prbType):
        return FORTIFICATION_ALIASES.STRONGHOLD_BATTLE_ROOM_VIEW_UI

    def getFlashAliases(self):
        return FORTIFICATION_ALIASES.FLASH_ALIASES

    def getPythonAliases(self):
        return FORTIFICATION_ALIASES.PYTHON_ALIASES

    def getPrbType(self):
        return PREBATTLE_TYPE.EXTERNAL

    def autoSearchCancel(self, value):
        self.currentState = value
        if value in (CYBER_SPORT_ALIASES.AUTO_SEARCH_COMMANDS_STATE, CYBER_SPORT_ALIASES.AUTO_SEARCH_ERROR_STATE, CYBER_SPORT_ALIASES.AUTO_SEARCH_WAITING_PLAYERS_STATE):
            self.prbEntity.request(AutoSearchUnitCtx(action=0))
        elif value == CYBER_SPORT_ALIASES.AUTO_SEARCH_CONFIRMATION_STATE:
            self.prbEntity.request(DeclineSearchUnitCtx())
        elif value == CYBER_SPORT_ALIASES.AUTO_SEARCH_ENEMY_STATE:
            self.prbEntity.request(BattleQueueUnitCtx(action=0))

    def onUnitPlayerAdded(self, pInfo):
        if not pInfo.isInvite():
            self.__addPlayerNotification(settings.UNIT_NOTIFICATION_KEY.PLAYER_ADDED, pInfo)

    def onUnitPlayerRemoved(self, pInfo):
        if not pInfo.isInvite():
            self.__addPlayerNotification(settings.UNIT_NOTIFICATION_KEY.PLAYER_REMOVED, pInfo)

    def onUnitFlagsChanged(self, flags, timeLeft):
        self.__registerOnMatchmakingTimerChangedListener()
        if self.prbEntity.hasLockedState():
            if flags.isInQueue():
                self.as_enableWndCloseBtnS(False)
                self.currentState = CYBER_SPORT_ALIASES.AUTO_SEARCH_ENEMY_STATE
            else:
                LOG_ERROR('View for modal state is not resolved', flags)
            self.__autosearchTimer = timeLeft
            self.__initState(timeDirection=-1)
            self.as_changeAutoSearchMainLabelS(i18n.makeString(TOOLTIPS.STRONGHOLDS_TIMER_WAITINGFORDATA))
            self.prbEntity.forceTimerEvent()
        else:
            self.__clearState()

    def onUnitErrorReceived(self, errorCode):
        self.as_autoSearchEnableBtnS(True)

    def onUnitAutoSearchFinished(self):
        self.__clearState()

    def onUnitPlayerRolesChanged(self, pInfo, pPermissions):
        if pInfo.isCurrentPlayer():
            self.as_changeAutoSearchBtnsStateS(pPermissions.canInvokeAutoSearch(), pPermissions.canStopBattleQueue())
        self.prbEntity.strongholdDataChanged()

    def onUnitPlayerOnlineStatusChanged(self, pInfo):
        super(StrongholdBattleRoomWindow, self).onUnitPlayerOnlineStatusChanged(pInfo)
        if pInfo.isOffline():
            key = settings.UNIT_NOTIFICATION_KEY.PLAYER_OFFLINE
        else:
            key = settings.UNIT_NOTIFICATION_KEY.PLAYER_ONLINE
        self.__addPlayerNotification(key, pInfo)

    def onUnitRejoin(self):
        self.__clearState()

    def onUnitPlayerBecomeCreator(self, pInfo):
        if pInfo.isCurrentPlayer():
            self._showLeadershipNotification()
        super(StrongholdBattleRoomWindow, self).onUnitPlayerBecomeCreator(pInfo)

    def refresh(self):
        self.prbEntity.requestMaintenanceUpdate()

    def onStrongholdOnReadyStateChanged(self):
        g_eventDispatcher.updateUI()

    def showStrongholdWaiting(self, visible):
        self.as_setWaitingS(visible, '#waiting:prebattle/change_settings')
        g_eventDispatcher.updateUI()

    def onStrongholdMaintenance(self, showWindow):
        if showWindow:
            text = str().join((icons.makeImageTag(RES_ICONS.MAPS_ICONS_LIBRARY_ALERTBIGICON, 24, 24, -6, 0),
             text_styles.middleTitle(i18n.makeString(FORTIFICATIONS.MAINWINDOW_MAINTENANCE_HEADER)),
             clans_fmts.getHtmlLineDivider(10),
             text_styles.main(i18n.makeString(FORTIFICATIONS.MAINWINDOW_MAINTENANCE_BODY))))
            self.as_setInfoS(True, text, FORTIFICATIONS.MAINWINDOW_MAINTENANCE_BUTTON)
            self.as_enableWndCloseBtnS(True)
        else:
            self.as_setInfoS(False, '', '')
            self.showStrongholdWaiting(True)
        g_eventDispatcher.updateUI()

    def onStrongholdDataChanged(self, header, isFirstBattle, reserve, reserveOrder):
        self.__registerOnMatchmakingTimerChangedListener()

    def _onRegisterFlashComponent(self, viewPy, alias):
        super(StrongholdBattleRoomWindow, self)._onRegisterFlashComponent(viewPy, alias)
        if isinstance(viewPy, StrongholdBattleRoom):
            viewPy.setProxy(self)

    def _populate(self):
        selectorUtils.setBattleTypeAsKnown(SELECTOR_BATTLE_TYPES.SORTIE)
        self.addListener(events.HideWindowEvent.HIDE_UNIT_WINDOW, self.__handleUnitWindowHide, scope=EVENT_BUS_SCOPE.LOBBY)
        self.addListener(events.RenameWindowEvent.RENAME_WINDOW, self.__handleWindowRename, scope=EVENT_BUS_SCOPE.LOBBY)
        super(StrongholdBattleRoomWindow, self)._populate()
        self.prbEntity.initEvents(self)
        g_eventDispatcher.hideUnitProgressInCarousel(self.getPrbType())

    def _dispose(self):
        self.removeListener(events.HideWindowEvent.HIDE_UNIT_WINDOW, self.__handleUnitWindowHide, scope=EVENT_BUS_SCOPE.LOBBY)
        self.removeListener(events.RenameWindowEvent.RENAME_WINDOW, self.__handleWindowRename, scope=EVENT_BUS_SCOPE.LOBBY)
        self.removeListener(events.StrongholdEvent.STRONGHOLD_ON_TIMER, self._onMatchmakingTimerChanged, scope=EVENT_BUS_SCOPE.STRONGHOLD)
        super(StrongholdBattleRoomWindow, self)._dispose()

    def _onMatchmakingTimerChanged(self, event):
        if self.__autosearchTimer is not None and self.currentState and self.prbEntity.hasLockedState():
            data = event.ctx
            timerState = data['textid']
            if data['dtime'] > 0 and timerState == TOOLTIPS.STRONGHOLDS_TIMER_SQUADINQUEUE:
                self.as_changeAutoSearchMainLabelS(i18n.makeString(CYBERSPORT.WINDOW_AUTOSEARCH_SEARCHENEMY_MAINTEXT))
                self.as_changeAutoSearchCountDownSecondsS(data['dtime'])
            else:
                self.as_changeAutoSearchTimeDirectionS(1)
                _, unit = self.prbEntity.getUnit()
                startTimer = 0
                if unit:
                    timestamp = unit.getModalTimestamp()
                    if timestamp:
                        startTimer = max(0, int(time_utils.getCurrentTimestamp() - time_utils.makeLocalServerTime(timestamp)))
                        LOG_DEBUG('time direction change, timers: ', time_utils.getCurrentTimestamp(), time_utils.makeLocalServerTime(timestamp))
                self.as_changeAutoSearchCountDownSecondsS(startTimer)
                LOG_DEBUG('changeAutoSearchCountDownSeconds', startTimer)
                if data['isSortie'] or data['isFirstBattle']:
                    self.as_changeAutoSearchMainLabelS(i18n.makeString(TOOLTIPS.STRONGHOLDS_TIMER_SEARCHENEMY))
                else:
                    self.as_changeAutoSearchMainLabelS(i18n.makeString(CYBERSPORT.WINDOW_AUTOSEARCH_SEARCHENEMY_MAINTEXT))
                self.__autosearchTimer = None
        return

    def __registerOnMatchmakingTimerChangedListener(self):
        if not self.__isOnMatchmakingTimerChangedRegistered and self.prbEntity.isStrongholdSettingsValid():
            self.__isOnMatchmakingTimerChangedRegistered = True
            self.addListener(events.StrongholdEvent.STRONGHOLD_ON_TIMER, self._onMatchmakingTimerChanged, scope=EVENT_BUS_SCOPE.STRONGHOLD)

    def __handleUnitWindowHide(self, _):
        self.destroy()

    def __handleWindowRename(self, event):
        title = event.ctx['data']
        self.as_setWindowTitleS(title)

    def __initState(self, timeLeft = 0, acceptDelta = 0, timeDirection = 1):
        model = None
        if self.isPlayerInSlot():
            if self.currentState == CYBER_SPORT_ALIASES.AUTO_SEARCH_ENEMY_STATE:
                model = self.__createAutoUpdateModel(self.currentState, timeLeft, '', [], timeDirection)
            elif self.currentState == CYBER_SPORT_ALIASES.AUTO_SEARCH_ERROR_STATE:
                model = self.__createAutoUpdateModel(self.currentState, 0, '', [], timeDirection)
        if model is not None:
            self.as_changeAutoSearchStateS(model)
        return

    def __clearState(self):
        self.currentState = ''
        self.as_enableWndCloseBtnS(True)
        self.as_hideAutoSearchS()
        self.__autosearchTimer = None
        return

    def __createAutoUpdateModel(self, state, countDownSeconds, ctxMessage, playersReadiness, timeDirection = 1):
        permissions = self.prbEntity.getPermissions(unitMgrID=self.prbEntity.getID())
        model = {'state': state,
         'countDownSeconds': countDownSeconds,
         'contextMessage': ctxMessage,
         'playersReadiness': playersReadiness,
         'canInvokeAutoSearch': permissions.canInvokeAutoSearch(),
         'canInvokeBattleQueue': permissions.canStopBattleQueue(),
         'timeDirection': timeDirection}
        return model

    def __addPlayerNotification(self, key, pInfo):
        chat = self.chat
        if chat and not pInfo.isCurrentPlayer():
            chat.as_addMessageS(messages.getUnitPlayerNotification(key, pInfo))
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\fortifications\StrongholdBattleRoomWindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:46:57 St�edn� Evropa (letn� �as)
