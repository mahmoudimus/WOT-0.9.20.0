# 2017.08.29 21:46:23 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCTankCarousel.py
from gui.Scaleform.daapi.view.lobby.hangar.carousels import TankCarousel
from gui.Scaleform.daapi.view.lobby.hangar.carousels.basic.carousel_data_provider import BCCarouselDataProvider
from gui.Scaleform.daapi.view.lobby.vehicle_carousel.carousel_filter import CarouselFilter, CriteriesGroup
from debug_utils import LOG_DEBUG
from account_helpers.settings_core import settings_constants
import BigWorld

class BCCriteriesGroup(CriteriesGroup):

    def __init__(self):
        super(BCCriteriesGroup, self).__init__()

    def apply(self, vehicle):
        return True

    @staticmethod
    def isApplicableFor(vehicle):
        return True


class BCCarouselFilter(CarouselFilter):

    def __init__(self):
        super(BCCarouselFilter, self).__init__()
        self._criteriesGroups = (BCCriteriesGroup(),)

    def load(self):
        pass

    def isDefault(self, keys = None):
        return True

    def getFilters(self, keys = None):
        return {}


class BCTankCarousel(TankCarousel):

    def __init__(self):
        super(BCTankCarousel, self).__init__()
        self._carouselDPCls = BCCarouselDataProvider
        self._carouselFilterCls = BCCarouselFilter
        self._usedFilters = ()

    def _populate(self):
        super(BCTankCarousel, self)._populate()

    def _getFiltersVisible(self):
        return False

    def updateParams(self):
        pass

    def selectVehicle(self, idx):
        super(BCTankCarousel, self).selectVehicle(idx)
        from bootcamp.BootcampGarage import g_bootcampGarage
        g_bootcampGarage.checkSecondVehicleHintEnabled()

    def _onCarouselSettingsChange(self, diff):
        needRefreshHint = settings_constants.GAME.CAROUSEL_TYPE in diff or settings_constants.GAME.DOUBLE_CAROUSEL_TYPE in diff
        if needRefreshHint:
            from bootcamp.BootcampGarage import g_bootcampGarage
            g_bootcampGarage.highlightLobbyHint('SecondTank', False, True)
        super(BCTankCarousel, self)._onCarouselSettingsChange(diff)
        if needRefreshHint:
            BigWorld.callback(0.1, g_bootcampGarage.checkSecondVehicleHintEnabled)
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\bootcamp\BCTankCarousel.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:46:23 St�edn� Evropa (letn� �as)
