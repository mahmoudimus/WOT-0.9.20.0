# 2017.08.29 21:48:35 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/NotifierMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class NotifierMeta(BaseDAAPIComponent):

    def showDialog(self, kind, title, text, buttons, handlers):
        self._printOverrideError('showDialog')

    def showI18nDialog(self, kind, i18nKey, handlers):
        self._printOverrideError('showI18nDialog')
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\framework\entities\abstract\NotifierMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:48:35 Støední Evropa (letní èas)
