# 2017.08.29 21:46:22 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCResearchPanel.py
from gui.Scaleform.daapi.view.meta.BCResearchPanelMeta import BCResearchPanelMeta
from CurrentVehicle import g_currentVehicle
from gui.shared import event_dispatcher as shared_events
from debug_utils import LOG_ERROR, LOG_DEBUG

class BCResearchPanel(BCResearchPanelMeta):

    def __init__(self):
        super(BCResearchPanel, self).__init__()

    def _populate(self):
        super(BCResearchPanel, self)._populate()

    def goToResearch(self):
        LOG_DEBUG('BCResearchPanel::goToResearch')
        if g_currentVehicle.isPresent():
            shared_events.showResearchView(g_currentVehicle.item.intCD)
        else:
            LOG_ERROR('Current vehicle is not preset')

    def as_updateCurrentVehicleS(self, data):
        if 'isElite' in data:
            data['isElite'] = False
        super(BCResearchPanel, self).as_updateCurrentVehicleS(data)

    def as_setEliteS(self, isElite):
        super(BCResearchPanel, self).as_setEliteS(False)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\bootcamp\BCResearchPanel.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:46:23 Støední Evropa (letní èas)
