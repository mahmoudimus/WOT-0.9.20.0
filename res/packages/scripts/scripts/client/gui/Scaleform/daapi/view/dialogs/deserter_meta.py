# 2017.08.29 21:46:28 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/deserter_meta.py
from gui.Scaleform.daapi.view.dialogs import I18nConfirmDialogMeta
from gui.shared.events import ShowDialogEvent

class IngameDeserterDialogMeta(I18nConfirmDialogMeta):

    def __init__(self, key, additionalInfo = '', focusedID = None):
        super(IngameDeserterDialogMeta, self).__init__(key, messageCtx={'additionalInfo': additionalInfo}, focusedID=focusedID)
        self.__imagePath = '../maps/icons/battle/deserterLeaveBattle.png'
        self.__offsetY = 270

    def getEventType(self):
        return ShowDialogEvent.SHOW_DESERTER_DLG

    def getImagePath(self):
        return self.__imagePath

    def getOffsetY(self):
        return self.__offsetY
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\dialogs\deserter_meta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:46:28 Støední Evropa (letní èas)
