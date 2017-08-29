# 2017.08.29 21:46:34 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/MinimapGrid.py
import weakref
import Math
import ArenaType
from gui.Scaleform.daapi.view.meta.MinimapGridMeta import MinimapGridMeta
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore

class MinimapGrid(MinimapGridMeta):
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self):
        super(MinimapGrid, self).__init__()
        self._channel = None
        self._controller = None
        return

    def _populate(self):
        super(MinimapGrid, self)._populate()

    def _dispose(self):
        super(MinimapGrid, self)._dispose()

    def setController(self, controller):
        controller.activate()
        self._controller = weakref.ref(controller)

    def removeController(self):
        self._controller = lambda : None

    def setActive(self, active):
        self.as_clickEnabled(active)

    def setClick(self, x, y):
        controller = self._controller()
        if controller:
            command = controller.proto.unitChat.createByMapPos(x, y)
            controller.sendCommand(command)

    def addCommand(self, cmd):
        if cmd.isOnMinimap():
            self.as_addPointS(cmd.getMapPosX(), cmd.getMapPosY())

    def as_addMessageS(self, message):
        pass

    def as_setJoinedS(self, flag):
        pass
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\MinimapGrid.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:46:34 St�edn� Evropa (letn� �as)
