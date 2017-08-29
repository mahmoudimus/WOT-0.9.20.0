# 2017.08.29 21:45:56 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/epic_random/battle_loading.py
from gui.Scaleform.daapi.view.battle.shared.battle_loading import BattleLoading, BattleLoadingTipSetting

class EpicRandomBattleLoading(BattleLoading):

    def _getViewSettingByID(self, settingID):
        """ Get settings for view by type
        :return:
        """
        result = {}
        if settingID == BattleLoadingTipSetting.OPTIONS.TEXT:
            result.update({'leftTeamTitleLeft': -418,
             'rightTeamTitleLeft': 200,
             'tipTitleTop': 536,
             'tipBodyTop': 562,
             'showTableBackground': True,
             'showTipsBackground': False})
        else:
            result.update({'leftTeamTitleLeft': -468,
             'rightTeamTitleLeft': 255,
             'tipTitleTop': 366,
             'tipBodyTop': 397,
             'showTableBackground': False,
             'showTipsBackground': True})
        return result
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\battle\epic_random\battle_loading.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:45:56 St�edn� Evropa (letn� �as)
