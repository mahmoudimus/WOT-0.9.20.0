# 2017.08.29 21:46:23 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCSimpleDialog.py
from gui.Scaleform.daapi.view.dialogs.SimpleDialog import SimpleDialog
from gui.Scaleform.framework import ScopeTemplates

class BCSimpleDialog(SimpleDialog):

    def __init__(self, message, title, buttons, handler, dialogScope = ScopeTemplates.DEFAULT_SCOPE, timer = 0):
        super(BCSimpleDialog, self).__init__(message, title, buttons, handler, dialogScope=dialogScope, timer=timer)

    def _dispose(self):
        super(BCSimpleDialog, self)._dispose()

    def __showPrevHint(self):
        from bootcamp.Bootcamp import g_bootcamp
        if g_bootcamp.getLessonNum() < g_bootcamp.getContextIntParameter('researchFreeLesson'):
            from bootcamp.BootcampGarage import g_bootcampGarage
            g_bootcampGarage.showPrevHint()

    def onWindowClose(self):
        super(BCSimpleDialog, self).onWindowClose()
        self.__showPrevHint()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\bootcamp\BCSimpleDialog.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:46:23 Støední Evropa (letní èas)
