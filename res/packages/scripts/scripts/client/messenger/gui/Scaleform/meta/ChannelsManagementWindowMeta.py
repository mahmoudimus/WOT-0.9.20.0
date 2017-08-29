# 2017.08.29 21:51:00 Støední Evropa (letní èas)
# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/ChannelsManagementWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ChannelsManagementWindowMeta(AbstractWindowView):

    def getSearchLimitLabel(self):
        self._printOverrideError('getSearchLimitLabel')

    def searchToken(self, token):
        self._printOverrideError('searchToken')

    def joinToChannel(self, index):
        self._printOverrideError('joinToChannel')

    def createChannel(self, name, usePassword, password, retype):
        self._printOverrideError('createChannel')

    def as_freezSearchButtonS(self, isEnable):
        if self._isDAAPIInited():
            return self.flashObject.as_freezSearchButton(isEnable)

    def as_getDataProviderS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDataProvider()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\messenger\gui\Scaleform\meta\ChannelsManagementWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:51:00 Støední Evropa (letní èas)
