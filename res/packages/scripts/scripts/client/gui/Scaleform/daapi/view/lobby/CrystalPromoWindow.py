# 2017.08.29 21:46:32 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/CrystalPromoWindow.py
from account_helpers.AccountSettings import AccountSettings
from gui.Scaleform.daapi.view.meta.CrystalsPromoWindowMeta import CrystalsPromoWindowMeta
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.locale.RES_ICONS import RES_ICONS

class CrystalsPromoWindow(CrystalsPromoWindowMeta):

    def __init__(self, ctx = None):
        super(CrystalsPromoWindow, self).__init__()

    def onWindowClose(self):
        self.destroy()

    def _dispose(self):
        super(CrystalsPromoWindow, self)._dispose()

    def _populate(self):
        super(CrystalsPromoWindow, self)._populate()
        self.as_setDataS({'windowTitle': MENU.CRYSTALS_PROMOWINDOW_TITLE,
         'headerTF': MENU.CRYSTALS_PROMOWINDOW_HEADER,
         'subTitle0': MENU.CRYSTALS_PROMOWINDOW_SUBTITLE0,
         'subDescr0': MENU.CRYSTALS_PROMOWINDOW_SUBDESCR0,
         'subTitle1': MENU.CRYSTALS_PROMOWINDOW_SUBTITLE1,
         'subDescr1': MENU.CRYSTALS_PROMOWINDOW_SUBDESCR1,
         'subTitle2': MENU.CRYSTALS_PROMOWINDOW_SUBTITLE2,
         'subDescr2': MENU.CRYSTALS_PROMOWINDOW_SUBDESCR2,
         'closeBtn': MENU.CRYSTALS_PROMOWINDOW_CLOSEBTN,
         'image0': RES_ICONS.MAPS_ICONS_BATTLETYPES_64X64_RANKED_EPICRANDOM,
         'image1': RES_ICONS.MAPS_ICONS_LIBRARY_CRYSTAL_80X80,
         'image2': RES_ICONS.MAPS_ICONS_MODULES_LISTOVERLAYSMALL,
         'bg': RES_ICONS.MAPS_ICONS_WINDOWS_CRYSTALSPROMOBG})
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\CrystalPromoWindow.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:46:32 St�edn� Evropa (letn� �as)
