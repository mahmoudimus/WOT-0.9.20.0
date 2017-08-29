# 2017.08.29 21:46:29 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/IconPriceDialog.py
from gui.Scaleform.daapi.view.meta.IconPriceDialogMeta import IconPriceDialogMeta
from gui.Scaleform.locale.DIALOGS import DIALOGS
from helpers import i18n
from gui.shared.formatters import getItemPricesVO

class IconPriceDialog(IconPriceDialogMeta):

    def __init__(self, meta, handler):
        super(IconPriceDialog, self).__init__(meta, handler)

    def _populate(self):
        super(IconPriceDialog, self)._populate()
        self.as_setPriceLabelS(i18n.makeString(DIALOGS.REMOVECONFIRMATIONNOTREMOVABLEMONEY_MESSAGEPRICE))
        itemPrice = self._meta.getMessagePrice()
        pricesVO = getItemPricesVO(itemPrice)
        self.as_setMessagePriceS({'itemPrices': pricesVO,
         'actionPrice': self._meta.getAction()})
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\dialogs\IconPriceDialog.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:46:29 Støední Evropa (letní èas)
