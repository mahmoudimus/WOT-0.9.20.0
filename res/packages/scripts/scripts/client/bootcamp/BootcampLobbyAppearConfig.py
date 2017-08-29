# 2017.08.29 21:43:46 Støední Evropa (letní èas)
# Embedded file name: scripts/client/bootcamp/BootcampLobbyAppearConfig.py
from gui.Scaleform.framework import ViewTypes
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS

class Appear:
    TOP = 1
    LEFT = 2
    RIGHT = 4
    BOTTOM = 8
    ALPHA = 16
    SCALE = 32


class BootcampLobbyAppearConfig:
    objects = {'Header': {'type': Appear.TOP},
     'HangarCrew': {'type': Appear.LEFT | Appear.ALPHA},
     'HangarQuestControl': {'type': Appear.TOP | Appear.ALPHA},
     'HeaderSilver': {'type': Appear.ALPHA},
     'HeaderGold': {'type': Appear.ALPHA},
     'MenuTechTree': {'type': Appear.ALPHA},
     'MenuHangar': {'type': Appear.TOP | Appear.ALPHA},
     'HeaderBattleSelector': {'type': Appear.ALPHA},
     'HeaderPremium': {'type': Appear.ALPHA},
     'HeaderMainMenuButtonBar': {'type': Appear.TOP | Appear.ALPHA},
     'HangarCarousel': {'type': Appear.BOTTOM}}

    def getItems(self):
        return self.objects


g_bootcampAppearConfig = BootcampLobbyAppearConfig()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\bootcamp\BootcampLobbyAppearConfig.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:43:46 Støední Evropa (letní èas)
