# 2017.08.29 21:43:49 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/bootcamp/StartBootcampTransition.py
import GUI
from gui import g_guiResetters
from gui.Scaleform.locale.BOOTCAMP import BOOTCAMP
from gui.Scaleform.genConsts.ROOT_SWF_CONSTANTS import ROOT_SWF_CONSTANTS
from gui.Scaleform.daapi.view.meta.StartBootcampTransitionMeta import StartBootcampTransitionMeta
from gui.Scaleform.daapi.view.external_components import ExternalFlashComponent
from gui.Scaleform.daapi.view.external_components import ExternalFlashSettings

class StartBootcampTransition(ExternalFlashComponent, StartBootcampTransitionMeta):

    def __init__(self, name):
        super(StartBootcampTransition, self).__init__(ExternalFlashSettings('transitionFlash', name, 'root.main', ROOT_SWF_CONSTANTS.BOOTCAMP_TRANISITION_CALLBACK))
        self.movie.scaleMode = 'NoScale'

    def _populate(self):
        super(StartBootcampTransition, self)._populate()
        self.__onUpdateStage()
        g_guiResetters.add(self.__onUpdateStage)
        self.as_setTransitionTextS(BOOTCAMP.TRANSITION_TITLE)

    def _dispose(self):
        g_guiResetters.discard(self.__onUpdateStage)
        super(StartBootcampTransition, self)._dispose()

    def __onUpdateStage(self):
        width, height = GUI.screenResolution()
        self.as_updateStageS(width, height)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\bootcamp\StartBootcampTransition.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:43:49 St�edn� Evropa (letn� �as)
