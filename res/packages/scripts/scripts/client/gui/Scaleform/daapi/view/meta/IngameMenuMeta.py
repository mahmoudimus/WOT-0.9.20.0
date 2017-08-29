# 2017.08.29 21:48:14 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/IngameMenuMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class IngameMenuMeta(AbstractWindowView):

    def quitBattleClick(self):
        self._printOverrideError('quitBattleClick')

    def settingsClick(self):
        self._printOverrideError('settingsClick')

    def helpClick(self):
        self._printOverrideError('helpClick')

    def cancelClick(self):
        self._printOverrideError('cancelClick')

    def onCounterNeedUpdate(self):
        self._printOverrideError('onCounterNeedUpdate')

    def bootcampClick(self):
        self._printOverrideError('bootcampClick')

    def as_setServerSettingS(self, serverName, tooltipFullData, serverState):
        if self._isDAAPIInited():
            return self.flashObject.as_setServerSetting(serverName, tooltipFullData, serverState)

    def as_setServerStatsS(self, stats, tooltipType):
        if self._isDAAPIInited():
            return self.flashObject.as_setServerStats(stats, tooltipType)

    def as_setCounterS(self, counters):
        """
        :param counters: Represented by Vector.<CountersVo> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setCounter(counters)

    def as_removeCounterS(self, counters):
        """
        :param counters: Represented by Vector.<String> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_removeCounter(counters)

    def as_setMenuButtonsLabelsS(self, helpLabel, settingsLabel, cancelLabel, quitLabel, bootcampLabel, bootcampIcon):
        if self._isDAAPIInited():
            return self.flashObject.as_setMenuButtonsLabels(helpLabel, settingsLabel, cancelLabel, quitLabel, bootcampLabel, bootcampIcon)

    def as_showQuitButtonS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showQuitButton(value)

    def as_showBootcampButtonS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showBootcampButton(value)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\IngameMenuMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:14 St�edn� Evropa (letn� �as)
