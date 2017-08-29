# 2017.08.29 21:46:59 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/filter_popover.py
import itertools
import constants
from account_helpers.settings_core import settings_constants
from account_helpers.settings_core.ServerSettingsManager import SETTINGS_SECTIONS
from gui import GUI_NATIONS
from gui.Scaleform import getNationsFilterAssetPath, getVehicleTypeAssetPath, getLevelsAssetPath, getButtonsAssetPath
from gui.Scaleform.daapi.view.lobby.hangar.filter_contexts import FilterSetupContext, getFilterPopoverSetupContexts
from gui.Scaleform.daapi.view.meta.TankCarouselFilterPopoverMeta import TankCarouselFilterPopoverMeta
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.prb_control.settings import VEHICLE_LEVELS
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER
from gui.shared.formatters import text_styles
from gui.shared.utils.functions import makeTooltip
from helpers import dependency
from helpers.i18n import makeString as _ms
from shared_utils import CONST_CONTAINER
from skeletons.gui.shared import IItemsCache
from skeletons.account_helpers.settings_core import ISettingsCore

class _SECTION(CONST_CONTAINER):
    NATIONS, VEHICLE_TYPES, LEVELS, SPECIALS, HIDDEN, TEXT_SEARCH = range(0, 6)


_VEHICLE_LEVEL_FILTERS = [ 'level_{}'.format(level) for level in VEHICLE_LEVELS ]

class VehiclesFilterPopover(TankCarouselFilterPopoverMeta):
    """ Base vehicle carousel filter popover for embedding in interfaces.
    
    There is a sections mechanism in this class. The main idea is that
    all the filters are placed in different sections (like, nations section,
    vehicles section, levels section, etc), and each section has its own id
    (defined in _SECTIONS). Each filter option (item) inside section has an
    id too (i.e. index).
    
    Flash sends updates in form of (sectionId, itemId), without the value,
    and we simply switch corresponding filter.
    
    The mapping (belongings of filters to sections) is calculated on runtime
    during popover initialization (because content of sections may vary).
    """
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, ctx):
        super(VehiclesFilterPopover, self).__init__()
        self._carousel = None
        self.__mapping = {}
        self.__usedFilters = ()
        return

    def setTankCarousel(self, carousel):
        """ Set tank carousel to the popover.
        
        This method is called on popover view load and substitutes _populate method,
        because all necessary data comes from carousel.
        
        :param tankCarousel: instance of CarouselEnvironment
        """
        self.__mapping = self._generateMapping(carousel.hasRentedVehicles(), carousel.hasEventVehicles())
        self.__usedFilters = list(itertools.chain.from_iterable(self.__mapping.itervalues()))
        self._carousel = carousel
        self._update(isInitial=True)

    def changeFilter(self, sectionId, itemId):
        """Switch boolean value of the filter entry.
        
        :param sectionId: id of the section defined in _SECTION
        :param itemId: index of the filter inside self._mapping
        """
        self._carousel.filter.switch(self.__mapping[sectionId][itemId], save=False)
        self._update()

    def changeSearchNameVehicle(self, inputText):
        self._carousel.filter.update({'searchNameVehicle': inputText}, save=False)
        self._update()

    def _getUpdateVO(self, filters):
        mapping = self.__mapping
        return {'nations': [ filters[key] for key in mapping[_SECTION.NATIONS] ],
         'vehicleTypes': [ filters[key] for key in mapping[_SECTION.VEHICLE_TYPES] ],
         'levels': [ filters[key] for key in mapping[_SECTION.LEVELS] ],
         'specials': [ filters[key] for key in mapping[_SECTION.SPECIALS] ],
         'hidden': [ filters[key] for key in mapping[_SECTION.HIDDEN] ]}

    def _getInitialVO(self, filters, xpRateMultiplier):
        mapping = self.__mapping
        dataVO = {'nationsSectionId': _SECTION.NATIONS,
         'vehicleTypesSectionId': _SECTION.VEHICLE_TYPES,
         'levelsSectionId': _SECTION.LEVELS,
         'specialSectionId': _SECTION.SPECIALS,
         'hiddenSectionId': _SECTION.HIDDEN,
         'titleLabel': text_styles.highTitle('#tank_carousel_filter:popover/title'),
         'nationsLabel': text_styles.standard('#tank_carousel_filter:popover/label/nations'),
         'vehicleTypesLabel': text_styles.standard('#tank_carousel_filter:popover/label/vehicleTypes'),
         'levelsLabel': text_styles.standard('#tank_carousel_filter:popover/label/levels'),
         'specialsLabel': text_styles.standard('#tank_carousel_filter:popover/label/specials'),
         'hiddenLabel': text_styles.standard('#tank_carousel_filter:popover/label/hidden'),
         'searchInputLabel': _ms('#tank_carousel_filter:popover/label/searchNameVehicle'),
         'searchInputName': filters.get('searchNameVehicle') or '',
         'searchInputTooltip': makeTooltip('#tank_carousel_filter:tooltip/searchInput/header', _ms('#tank_carousel_filter:tooltip/searchInput/body', count=50)),
         'searchInputMaxChars': 50,
         'nations': [],
         'vehicleTypes': [],
         'levels': [],
         'specials': [],
         'hidden': [],
         'hiddenSectionVisible': True,
         'specialSectionVisible': True}

        def isSelected(entry):
            return filters.get(entry, False)

        for entry in mapping[_SECTION.NATIONS]:
            dataVO['nations'].append({'value': getNationsFilterAssetPath(entry),
             'tooltip': makeTooltip('#nations:{}'.format(entry), '#tank_carousel_filter:tooltip/nations/body'),
             'selected': isSelected(entry)})

        for entry in mapping[_SECTION.LEVELS]:
            dataVO['levels'].append({'value': getLevelsAssetPath(entry),
             'selected': isSelected(entry)})

        for entry in mapping[_SECTION.VEHICLE_TYPES]:
            dataVO['vehicleTypes'].append({'value': getVehicleTypeAssetPath(entry),
             'tooltip': makeTooltip('#menu:carousel_tank_filter/{}'.format(entry), '#tank_carousel_filter:tooltip/vehicleTypes/body'),
             'selected': isSelected(entry)})

        for entry in mapping[_SECTION.HIDDEN]:
            dataVO['hidden'].append({'label': text_styles.standard('#tank_carousel_filter:popover/checkbox/{}'.format(entry)),
             'tooltip': makeTooltip('#tank_carousel_filter:tooltip/{}/header'.format(entry), '#tank_carousel_filter:tooltip/{}/body'.format(entry)),
             'selected': isSelected(entry)})

        for entry in mapping[_SECTION.SPECIALS]:
            contexts = getFilterPopoverSetupContexts(xpRateMultiplier)
            filterCtx = contexts.get(entry, FilterSetupContext())
            dataVO['specials'].append({'value': getButtonsAssetPath(filterCtx.asset or entry),
             'tooltip': makeTooltip('#tank_carousel_filter:tooltip/{}/header'.format(entry), _ms('#tank_carousel_filter:tooltip/{}/body'.format(entry), **filterCtx.ctx)),
             'selected': isSelected(entry)})

        if not dataVO['hidden']:
            dataVO['hiddenSectionVisible'] = False
        if not dataVO['specials']:
            dataVO['specialSectionVisible'] = False
        return dataVO

    def _dispose(self):
        if self._carousel is not None and self._carousel.filter is not None:
            self._carousel.filter.save()
            self._carousel.blinkCounter()
            self._carousel = None
        self.__mapping = {}
        self.__usedFilters = ()
        super(VehiclesFilterPopover, self)._dispose()
        return

    def _update(self, isInitial = False):
        """ Update state of the flash.
        
        :param isInitial: boolean, specifies whether flash should be initialized or updated
        """
        filters = self._carousel.filter.getFilters(self.__usedFilters)
        xpRateMultiplier = self.itemsCache.items.shop.dailyXPFactor
        if isInitial:
            self.as_setInitDataS(self._getInitialVO(filters, xpRateMultiplier))
        else:
            self.as_setStateS(self._getUpdateVO(filters))
        self._carousel.applyFilter()
        self.as_showCounterS(text_styles.main(_ms('#tank_carousel_filter:popover/counter', count=self._carousel.formatCountVehicles())))

    @classmethod
    def _generateMapping(cls, hasRented, hasEvent):
        """ Generate mapping of currently used filters to the sections in popover.
        
        :param hasRented: boolean, specifies whether rented checkbox should appear in popover
        :param hasEvent: boolean, specifies whether event checkbox should appear in popover
        """
        mapping = {_SECTION.NATIONS: GUI_NATIONS,
         _SECTION.VEHICLE_TYPES: VEHICLE_TYPES_ORDER,
         _SECTION.LEVELS: _VEHICLE_LEVEL_FILTERS,
         _SECTION.SPECIALS: [],
         _SECTION.HIDDEN: [],
         _SECTION.TEXT_SEARCH: ['searchNameVehicle']}
        if hasRented:
            mapping[_SECTION.HIDDEN].append('rented')
        if hasEvent:
            mapping[_SECTION.HIDDEN].append('event')
        return mapping


class TankCarouselFilterPopover(VehiclesFilterPopover):
    """ Filter popover for hangar's tank carousel (supports row count switching).
    """
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self, ctx):
        super(TankCarouselFilterPopover, self).__init__(ctx)
        setting = self.settingsCore.options.getSetting(settings_constants.GAME.CAROUSEL_TYPE)
        self.__carouselRowCount = setting.get()

    def switchCarouselType(self, selected):
        setting = self.settingsCore.options.getSetting(settings_constants.GAME.CAROUSEL_TYPE)
        self.__carouselRowCount = setting.CAROUSEL_TYPES.index(setting.OPTIONS.DOUBLE if selected else setting.OPTIONS.SINGLE)
        self._carousel.setRowCount(self.__carouselRowCount + 1)

    def _getInitialVO(self, filters, xpRateMultiplier):
        dataVO = super(TankCarouselFilterPopover, self)._getInitialVO(filters, xpRateMultiplier)
        dataVO.update({'toggleSwitchCarouselTooltip': makeTooltip('#tank_carousel_filter:tooltip/toggleSwitchCarousel/header', '#tank_carousel_filter:tooltip/toggleSwitchCarousel/body'),
         'toggleSwitchCarouselIcon': RES_ICONS.MAPS_ICONS_FILTERS_DOUBLE_CAROUSEL,
         'toggleSwitchCarouselSelected': bool(self.__carouselRowCount)})
        return dataVO

    def _update(self, isInitial = False):
        super(TankCarouselFilterPopover, self)._update(isInitial)
        self._carousel.updateHotFilters()

    def _dispose(self):
        super(TankCarouselFilterPopover, self)._dispose()
        self.settingsCore.serverSettings.setSectionSettings(SETTINGS_SECTIONS.GAME_EXTENDED, {settings_constants.GAME.CAROUSEL_TYPE: self.__carouselRowCount})

    @classmethod
    def _generateMapping(cls, hasRented, hasEvent):
        mapping = super(TankCarouselFilterPopover, cls)._generateMapping(hasRented, hasEvent)
        mapping[_SECTION.SPECIALS].extend(['bonus',
         'favorite',
         'premium',
         'elite'])
        if constants.IS_KOREA:
            mapping[_SECTION.SPECIALS].append('igr')
        return mapping
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\hangar\filter_popover.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:46:59 St�edn� Evropa (letn� �as)
