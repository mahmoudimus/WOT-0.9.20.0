# 2017.08.29 21:45:50 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/settings.py
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from shared_utils import CONST_CONTAINER

class ICONS_SIZES(CONST_CONTAINER):
    X80 = '80x80'
    X48 = '48x48'
    X24 = '24x24'


class BADGES_ICONS(CONST_CONTAINER):
    X80 = ICONS_SIZES.X80
    X48 = ICONS_SIZES.X48
    X24 = ICONS_SIZES.X24


def getBadgeIconPath(size, badgeID):
    return RES_ICONS.getBadgeIcon(size, badgeID)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\settings.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:45:50 Støední Evropa (letní èas)
