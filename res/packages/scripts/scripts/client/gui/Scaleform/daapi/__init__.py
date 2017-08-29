# 2017.08.29 21:45:51 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/__init__.py
from gui.Scaleform.framework.entities.View import View

class LobbySubView(View):
    __background_alpha__ = 0.6

    def setEnvironment(self, app):
        app.setBackgroundAlpha(self.__background_alpha__)
        super(LobbySubView, self).setEnvironment(app)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:45:51 Støední Evropa (letní èas)
