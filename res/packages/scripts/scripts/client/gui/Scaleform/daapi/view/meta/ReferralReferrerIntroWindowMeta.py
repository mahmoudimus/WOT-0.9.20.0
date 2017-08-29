# 2017.08.29 21:48:22 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ReferralReferrerIntroWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ReferralReferrerIntroWindowMeta(AbstractWindowView):

    def onClickApplyButton(self):
        self._printOverrideError('onClickApplyButton')

    def onClickHrefLink(self):
        self._printOverrideError('onClickHrefLink')

    def as_setDataS(self, data):
        """
        :param data: Represented by ReferralReferrerIntroVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\meta\ReferralReferrerIntroWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:22 Støední Evropa (letní èas)
