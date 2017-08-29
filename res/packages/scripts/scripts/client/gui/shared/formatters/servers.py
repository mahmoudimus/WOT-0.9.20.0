# 2017.08.29 21:49:33 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/shared/formatters/servers.py
import constants
from gui import makeHtmlString
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.shared.formatters import icons
from gui.shared.formatters import text_styles
from predefined_hosts import HOST_AVAILABILITY, PING_STATUSES
_UNAVAILABLE_DATA_PLACEHOLDER = '--'

def formatPingStatus(csisStatus, isColorBlind, isSelected, pingStatus, pingValue, useBigSize = False):
    """
    
    :param csisStatus:
    :param isColorBlind:
    :param isSelected:
    :param pingStatus:
    :param pingValue:
    :param useBigSize: If True result str has 14 font size, otherwise - 11 font size
    :return:
    """
    if pingStatus == PING_STATUSES.REQUESTED:
        return None
    else:
        if csisStatus != HOST_AVAILABILITY.NOT_AVAILABLE and pingStatus != PING_STATUSES.UNDEFINED:
            if pingStatus == PING_STATUSES.LOW:
                formattedPing = text_styles.goodPing(pingValue)
            else:
                formattedPing = text_styles.main(pingValue) if isSelected else text_styles.standartPing(pingValue)
        else:
            pingValue = _UNAVAILABLE_DATA_PLACEHOLDER
            pingStatus = PING_STATUSES.UNDEFINED
            formattedPing = text_styles.standard(pingValue)
        colorBlindName = ''
        if isColorBlind and pingStatus == PING_STATUSES.HIGH:
            colorBlindName = '_color_blind'
        pingStatusIcon = formatPingStatusIcon(RES_ICONS.maps_icons_pingstatus_stairs_indicator(str(pingStatus) + colorBlindName + '.png'))
        if useBigSize:
            return text_styles.concatStylesToSingleLine(text_styles.main(' '), formattedPing, pingStatusIcon)
        return text_styles.concatStylesToSingleLine(formattedPing, '', pingStatusIcon)
        return None


def formatPingStatusIcon(icon):
    return icons.makeImageTag(icon, 14, 14, -3)


def wrapServerName(name):
    if constants.IS_CHINA:
        return makeHtmlString('html_templates:lobby/serverStats', 'serverName', {'name': name})
    return name
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\formatters\servers.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:49:33 Støední Evropa (letní èas)
