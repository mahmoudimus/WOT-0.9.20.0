# 2017.08.29 21:48:21 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RankedBattlesCalendarPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class RankedBattlesCalendarPopoverMeta(SmartPopOverView):

    def onDaySelect(self, date):
        self._printOverrideError('onDaySelect')

    def as_setDataS(self, data):
        """
        :param data: Represented by RankedBattlesCalendarVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setDayDataS(self, data):
        """
        :param data: Represented by RankedBattlesCalendarDayVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDayData(data)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\RankedBattlesCalendarPopoverMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:21 Støední Evropa (letní èas)
