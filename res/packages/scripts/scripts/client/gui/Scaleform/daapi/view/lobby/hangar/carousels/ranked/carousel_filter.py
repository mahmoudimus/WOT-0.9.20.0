# 2017.08.29 21:47:04 Støední Evropa (letní èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/ranked/carousel_filter.py
from account_helpers.AccountSettings import RANKED_CAROUSEL_FILTER_1, RANKED_CAROUSEL_FILTER_2
from account_helpers.AccountSettings import RANKED_CAROUSEL_FILTER_CLIENT_1
from gui.Scaleform.daapi.view.lobby.vehicle_carousel.carousel_filter import CarouselFilter

class RankedCarouselFilter(CarouselFilter):

    def __init__(self):
        super(RankedCarouselFilter, self).__init__()
        self._serverSections = (RANKED_CAROUSEL_FILTER_1, RANKED_CAROUSEL_FILTER_2)
        self._clientSections = (RANKED_CAROUSEL_FILTER_CLIENT_1,)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\hangar\carousels\ranked\carousel_filter.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:47:04 Støední Evropa (letní èas)
