# 2017.08.29 21:48:07 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanProfileMainWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ClanProfileMainWindowMeta(AbstractWindowView):

    def as_setDataS(self, data):
        """
        :param data: Represented by ClanProfileMainWindowVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setWindowTitleS(self, title):
        if self._isDAAPIInited():
            return self.flashObject.as_setWindowTitle(title)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\ClanProfileMainWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:07 St�edn� Evropa (letn� �as)
