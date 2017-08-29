# 2017.08.29 21:51:59 Støední Evropa (letní èas)
# Embedded file name: scripts/client/tutorial/gui/Scaleform/battle_v2/settings.py
from gui.Scaleform.framework import GroupedViewSettings, ViewTypes, ScopeTemplates
from tutorial.gui.Scaleform.battle_v2.pop_ups import ReplenishAmmoDialog

class BATTLE_VIEW_ALIAS(object):
    REPLENISH_AMMO_DIALOG = 'replenishAmmoDialog'


BATTLE_VIEW_SETTINGS = (GroupedViewSettings(BATTLE_VIEW_ALIAS.REPLENISH_AMMO_DIALOG, ReplenishAmmoDialog, 'replenishAmmoDialog.swf', ViewTypes.TOP_WINDOW, '', None, ScopeTemplates.DEFAULT_SCOPE, isModal=True, canClose=False, isCentered=False),)
DIALOG_ALIAS_MAP = {'replenishAmmo': BATTLE_VIEW_ALIAS.REPLENISH_AMMO_DIALOG}
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\tutorial\gui\Scaleform\battle_v2\settings.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:51:59 Støední Evropa (letní èas)
