# 2017.08.29 21:51:00 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/FAQWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FAQWindowMeta(AbstractWindowView):

    def onLinkClicked(self, name):
        self._printOverrideError('onLinkClicked')

    def as_appendTextS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_appendText(text)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\messenger\gui\Scaleform\meta\FAQWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:51:00 St�edn� Evropa (letn� �as)
