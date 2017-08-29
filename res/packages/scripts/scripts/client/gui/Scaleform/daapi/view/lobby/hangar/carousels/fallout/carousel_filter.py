# 2017.08.29 21:47:03 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousels/fallout/carousel_filter.py
from account_helpers.AccountSettings import FALLOUT_CAROUSEL_FILTER_1, FALLOUT_CAROUSEL_FILTER_2
from gui.Scaleform.daapi.view.lobby.vehicle_carousel.carousel_filter import CarouselFilter, BasicCriteriesGroup, EventCriteriesGroup
from gui.shared.utils.requesters import REQ_CRITERIA

class FalloutCarouselFilter(CarouselFilter):

    def __init__(self):
        super(FalloutCarouselFilter, self).__init__()
        self._serverSections = (FALLOUT_CAROUSEL_FILTER_1, FALLOUT_CAROUSEL_FILTER_2)
        self._criteriesGroups = (EventCriteriesGroup(), FalloutBasicCriteriesGroup())


class FalloutBasicCriteriesGroup(BasicCriteriesGroup):

    def update(self, filters):
        super(FalloutBasicCriteriesGroup, self).update(filters)
        if filters['gameMode']:
            self._criteria |= REQ_CRITERIA.VEHICLE.FALLOUT.AVAILABLE
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\hangar\carousels\fallout\carousel_filter.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:47:03 St�edn� Evropa (letn� �as)
