# 2017.08.29 21:47:13 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/missions/conditions_formatters/requirements.py
import types
import BigWorld
import nations
from constants import EVENT_TYPE, IGR_TYPE, IS_CHINA
from gui import makeHtmlString
from gui.Scaleform.daapi.view.lobby.missions.conditions_formatters import packTokenProgress, packText, getSeparator, intersperse
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.server_events.cond_formatters.formatters import ConditionFormatter, ConditionsFormatter
from gui.server_events.conditions import GROUP_TYPE, AndGroup
from gui.server_events.formatters import TOKEN_SIZES
from gui.shared.formatters import text_styles, icons
from helpers import int2roman, dependency
from helpers.i18n import makeString as ms
from shared_utils import first
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache

def packTokens(tokens):
    return {'tokens': tokens}


def relate(relation, value, label):
    """ Add a relation information to the existing label.
    """
    if type(value) not in types.StringTypes:
        value = BigWorld.wg_getNiceNumberFormat(value)
    else:
        value = value
    relation = ms('#quests:details/requirementsRelation/{}'.format(relation))
    rlabel = ms('#quests:details/requirements/relation', relation=relation, value=value)
    return '{}{}'.format(label, rlabel)


def prepareAccountConditionsGroup(conditions, event):
    """
    Create union AND group condition for account requirements component
    contains account requirements and some specific vehicle requirements,
    which may be displayed in account requirements component WOTD-84729
    Wrap vehicle requirement in vehicle condition adapter, that check available for all suitable vehicles
    """
    group = AndGroup()
    group.add(conditions.getConditions())
    group.add(_getAdapter(event.vehicleReqs.getConditions(), event.vehicleReqs.getSuitableVehicles()))
    return group


def _isVehicleConditionAvailable(condition, suitableVehicles):
    for vehicle in suitableVehicles:
        if condition.isAvailable(vehicle):
            return True

    return False


def _getAdapter(condition, suitableVehicles):
    if condition.getName() == GROUP_TYPE.AND:
        return VehicleGroupAndAdapter(condition, suitableVehicles)
    elif condition.getName() == GROUP_TYPE.OR:
        return VehicleGroupOrAdapter(condition, suitableVehicles)
    else:
        return VehicleConditionAdapter(condition, suitableVehicles)


class RecursiveFormatter(ConditionsFormatter):
    """ Formatter meant to be called recursively by itself.
    
    Supports so-called gathering formatters, i.e. formatters that depend on
    current level of recursion nesting and should be instantiated on the current
    method level, not globally on class instance level.
    """

    def __init__(self, formatters = None, gatheringFormatters = None):
        super(RecursiveFormatter, self).__init__(formatters)
        self.__gatheringFormatters = gatheringFormatters or {}

    def createGatheringFormatters(self):
        result = {}
        for key, cls in self.__gatheringFormatters.iteritems():
            result[key] = cls()

        return result


class VehicleConditionAdapter(object):
    """
    Adapter for vehicle requirements
    Work as vehicle condition, but overrides isAvailable method in which check condition for all suitable vehicles
    """

    def __init__(self, condition, suitableVehicles):
        self._condition = condition
        self._suitableVehicles = suitableVehicles

    def isAvailable(self):
        return _isVehicleConditionAvailable(self._condition, self._suitableVehicles)

    def getName(self):
        return self._condition.getName()

    def getValue(self):
        return self._condition.getValue()


class VehicleGroupAdapter(VehicleConditionAdapter):
    """
    Adapter for vehicle requirements group
    Work as logical conditions group,
    but overrides isAvailable method in which check condition for all suitable vehicles
    """

    def isEmpty(self):
        return not len(self._condition.items)

    def getSortedItems(self):
        return [ _getAdapter(condition, self._suitableVehicles) for condition in self._condition.getSortedItems() ]


class VehicleGroupOrAdapter(VehicleGroupAdapter):
    """
    Adapter for OR vehicles conditions logical group
    """

    def isAvailable(self, *args, **kwargs):
        for cond in self._condition.items:
            if _isVehicleConditionAvailable(cond, self._suitableVehicles):
                return True

        return False


class VehicleGroupAndAdapter(VehicleGroupAdapter):
    """
    Adapter for AND vehicles conditions logical group
    """

    def isAvailable(self, *args, **kwargs):
        res = True
        for cond in self._condition.items:
            res = _isVehicleConditionAvailable(cond, self._suitableVehicles)
            if not res:
                return res

        return res


class AccountRequirementsFormatter(ConditionsFormatter):
    """
    Formatter for the account requirements block and some vehicles conditions block in the detailed quest window.
    Display vehicles conditions in account requirements block was additional UX request
    """

    def __init__(self):
        super(AccountRequirementsFormatter, self).__init__({'and': RecursiveGroupFormatter(),
         'or': RecursiveGroupFormatter(),
         'single': SingleGroupFormatter()})

    def format(self, conditions, event):
        if event.isGuiDisabled():
            return {}
        group = prepareAccountConditionsGroup(conditions, event)
        formatter = self._getGroupFormatter(group)
        requirements, passed, total = formatter.format(group, event)
        conclusion = formatter.conclusion(group, event, passed, total)
        if not requirements and not conclusion:
            return {}
        return {'header': conclusion,
         'requirements': requirements}

    def _getGroupFormatter(self, group):
        if len(group.items) == 1 and first(group.items).getName() not in ('token', 'and', 'or'):
            return self.getConditionFormatter('single')
        else:
            return self.getConditionFormatter(group.getName())


class TQAccountRequirementsFormatter(AccountRequirementsFormatter):
    """ Formatter for the account requirements block of token quest.
    
    The difference is that token requirements shouldn't appear in token quest.
    """

    def __init__(self):
        super(AccountRequirementsFormatter, self).__init__({'and': TQRecursiveGroupFormatter(),
         'or': TQRecursiveGroupFormatter(),
         'single': SingleGroupFormatter()})

    def _getGroupFormatter(self, group):
        return self.getConditionFormatter(group.getName())


class SingleGroupFormatter(ConditionsFormatter):
    """ Special formatter for the single-condition case.
    
    We display this single condition in the header, so the body is empty.
    """

    def __init__(self):
        super(SingleGroupFormatter, self).__init__({'premiumAccount': PremiumAccountFormatter(),
         'inClan': InClanRequirementFormatter(),
         'igrType': IgrTypeRequirementFormatter(),
         'GR': GlobalRatingRequirementFormatter(),
         'accountDossier': AccountDossierRequirementFormatter(),
         'vehiclesUnlocked': VehiclesRequirementFormatter(),
         'vehiclesOwned': VehiclesRequirementFormatter(),
         'hasReceivedMultipliedXP': HasReceivedMultipliedXPFormatter()})

    def conclusion(self, group, event, passed, total):
        """ Format the requirement header.
        """
        if group.isAvailable():
            icon = ''
            style = text_styles.standard
            header = '#quests:missionDetails/requirements/header/available'
        else:
            icon = (icons.makeImageTag(RES_ICONS.MAPS_ICONS_LIBRARY_MARKER_BLOCKED, width=14, height=14, vSpace=-1, hSpace=-2),)
            style = text_styles.error
            header = '#quests:missionDetails/requirements/header/unavailable'
        result = []
        for condition in group.getSortedItems():
            fmt = self.getConditionFormatter(condition.getName())
            if fmt:
                branch = fmt.format(condition, event, self._styler)
                result.extend(branch)

        result = (branch.get('text') for branch in result)
        reason = text_styles.concatStylesToMultiLine(*result)
        return text_styles.concatStylesWithSpace(icon, style(header), reason)

    def format(self, group, event):
        """ Format the requirement body.
        """
        passed = 0
        for condition in group.getSortedItems():
            if condition.isAvailable():
                passed += 1

        return ([], passed, len(group.items))

    @staticmethod
    def _styler(isRequirementMet):
        if isRequirementMet:
            return text_styles.standard
        else:
            return text_styles.main


class RecursiveGroupFormatter(RecursiveFormatter):
    """ Recursive formatter that walks over condition groups.
    """

    def __init__(self):
        super(RecursiveGroupFormatter, self).__init__(formatters={'premiumAccount': PremiumAccountFormatter(),
         'inClan': InClanRequirementFormatter(),
         'igrType': IgrTypeRequirementFormatter(),
         'GR': GlobalRatingRequirementFormatter(),
         'accountDossier': AccountDossierRequirementFormatter(),
         'vehiclesUnlocked': VehiclesRequirementFormatter(),
         'vehiclesOwned': VehiclesRequirementFormatter(),
         'hasReceivedMultipliedXP': HasReceivedMultipliedXPFormatter()}, gatheringFormatters={'token': TokenGatheringRequirementFormatter})

    def conclusion(self, group, event, passed, total):
        """ Format the requirement header.
        """
        if not total:
            return ''
        if group.isAvailable():
            icon = ''
            headerStyle = text_styles.standard
            reasonStyle = text_styles.standard
            header = '#quests:missionDetails/requirements/header/available'
            reason = '#quests:missionDetails/requirements/conclusion/available'
            count = total
        else:
            icon = (icons.makeImageTag(RES_ICONS.MAPS_ICONS_LIBRARY_MARKER_BLOCKED, width=14, height=14, vSpace=-1, hSpace=-2),)
            headerStyle = text_styles.error
            reasonStyle = text_styles.main
            header = '#quests:missionDetails/requirements/header/unavailable'
            reason = '#quests:missionDetails/requirements/conclusion/unavailable'
            count = total - passed
        return text_styles.concatStylesWithSpace(icon, headerStyle(header), reasonStyle(ms(reason, count=count)))

    def format(self, group, event, isNested = False):
        """ Format the requirement body.
        """
        result = []
        total, passed = (0, 0)
        separator = getSeparator(group.getName())
        gatheringFmts = self.createGatheringFormatters()
        for condition in group.getSortedItems():
            conditionName = condition.getName()
            if conditionName in GROUP_TYPE.ALL():
                branch, bpassed, btotal = self.format(condition, event, isNested=True)
                total += btotal
                passed += bpassed
            else:
                if conditionName in gatheringFmts:
                    fmt = gatheringFmts.get(conditionName)
                    fmt.gather(condition, event)
                    branch = []
                elif self.hasFormatter(conditionName):
                    fmt = self.getConditionFormatter(conditionName)
                    branch = fmt.format(condition, event, self._styler)
                else:
                    branch = []
                if branch:
                    total += 1
                    if condition.isAvailable():
                        passed += 1
            if branch:
                self._iconize(condition.isAvailable(), isNested, branch)
                result.extend(branch)

        for fmt in gatheringFmts.itervalues():
            branch = fmt.format(self._styler)
            if branch:
                total += 1
                self._iconize(fmt.isAvailable(), isNested, branch)
                result.extend(branch)

        if separator:
            result = intersperse(result, packText(separator))
        return (result, passed, total)

    @staticmethod
    def _styler(isRequirementMet):
        if isRequirementMet:
            return text_styles.success
        else:
            return text_styles.main

    @staticmethod
    def _iconize(isAvailable, isNested, branch):
        if isAvailable:
            icon = RES_ICONS.MAPS_ICONS_LIBRARY_OKICON
        else:
            icon = RES_ICONS.MAPS_ICONS_LIBRARY_CYBERSPORT_NOTAVAILABLEICON
        if not isNested and branch:
            branch[0].update(icon=icon)


class TQRecursiveGroupFormatter(RecursiveGroupFormatter):
    """ Recursive formatter that walks over condition groups in token quest.
    
    The difference is that it has no formatter for the token condition.
    """

    def __init__(self):
        super(RecursiveGroupFormatter, self).__init__(formatters={'premiumAccount': PremiumAccountFormatter(),
         'inClan': InClanRequirementFormatter(),
         'igrType': IgrTypeRequirementFormatter(),
         'GR': GlobalRatingRequirementFormatter(),
         'accountDossier': AccountDossierRequirementFormatter(),
         'vehiclesUnlocked': VehiclesRequirementFormatter(),
         'vehiclesOwned': VehiclesRequirementFormatter(),
         'hasReceivedMultipliedXP': HasReceivedMultipliedXPFormatter()})


class PremiumAccountFormatter(ConditionFormatter):

    @classmethod
    def format(cls, condition, event, styler):
        if condition.isPremiumNeeded():
            labelKey = 'premiumAccount'
        else:
            labelKey = 'notPremiumAccount'
        label = ms('#quests:details/requirements/{}'.format(labelKey))
        style = styler(condition.isAvailable())
        return [packText(style(label))]


class InClanRequirementFormatter(ConditionFormatter):
    itemsCache = dependency.descriptor(IItemsCache)

    @classmethod
    def format(cls, condition, event, styler):
        labelKey = None
        if condition.getClanIds() is None:
            if condition.isNegative():
                labelKey = 'notInAnyClan'
            else:
                labelKey = 'inAnyClan'
        else:
            clanDBID = cls.itemsCache.items.stats.clanDBID
            if not condition.isNegative():
                if clanDBID:
                    if clanDBID in condition.getClanIds():
                        labelKey = 'forCurrentClan'
                    else:
                        labelKey = 'notForCurrentClan'
                else:
                    labelKey = 'inClan'
            elif clanDBID and clanDBID in condition.getClanIds():
                labelKey = 'notForCurrentClan'
        if labelKey is not None:
            label = ms('#quests:details/requirements/{}'.format(labelKey))
            style = styler(condition.isAvailable())
            return [packText(style(label))]
        else:
            return []


class IgrTypeRequirementFormatter(ConditionFormatter):

    @classmethod
    def format(cls, condition, event, styler):
        igrTypes = condition.getIgrTypes()
        if IS_CHINA:
            key = 'igr'
        elif igrTypes.issubset({IGR_TYPE.BASE}):
            key = 'igrBasic'
        elif igrTypes.issubset({IGR_TYPE.PREMIUM}):
            key = 'igrPremium'
        else:
            key = 'igr'
        label = ms('#quests:details/requirements/{}'.format(key))
        style = styler(condition.isAvailable())
        return [packText(makeHtmlString('html_templates:lobby/quests', 'playInIgr', {'label': style(label)}))]


class GlobalRatingRequirementFormatter(ConditionFormatter):

    @classmethod
    def format(cls, condition, event, styler):
        relation, value = condition.relation, condition.relationValue
        label = ms('#quests:details/requirements/globalRating')
        label = relate(relation, value, label)
        style = styler(condition.isAvailable())
        return [packText(style(label))]


class VehiclesRequirementFormatter(ConditionFormatter):

    @classmethod
    def format(cls, condition, event, styler):
        style = styler(condition.isAvailable())
        labelKey = '#quests:details/requirements/{}'.format(condition.getName())
        result = []
        if condition.isAnyVehicleAcceptable():
            label = ms('{}/all'.format(labelKey))
            result.append(packText(style(label)))
        elif 'types' not in condition.data:
            _, fnations, flevels, fclasses = condition.parseFilters()
            keys, kwargs = [], {}
            if fnations:
                keys.append('nation')
                names = [ nations.NAMES[nationId] for nationId in fnations ]
                names = [ ms('#menu:nations/{}'.format(name)) for name in names ]
                kwargs['nation'] = ', '.join(names)
            if fclasses:
                keys.append('type')
                names = [ ms('#menu:classes/{}'.format(name)) for name in fclasses ]
                kwargs['type'] = ', '.join(names)
            if flevels:
                keys.append('level')
                names = [ int2roman(lvl) for lvl in flevels ]
                kwargs['level'] = ', '.join(names)
            labelKey = '{}/{}'.format(labelKey, '_'.join(keys))
            if condition.relationValue is None and condition.isNegative():
                labelKey = '{}/not'.format(labelKey)
            label = ms(labelKey, **kwargs)
            label = relate(condition.relation, condition.relationValue, label)
            result.append(packText(style(label)))
        else:
            if condition.isNegative():
                labelKey = '{}/not'.format(labelKey)
            label = ms(labelKey)
            names = [ vehicle.userName for vehicle in condition.getVehiclesList() ]
            result.append(packText(style('{}: {}'.format(label, ', '.join(names)))))
        return result


class HasReceivedMultipliedXPFormatter(ConditionFormatter):
    """
    Formatter for hasReceivedMultipliedXP vehicle requirement
    Although hasReceivedMultipliedXP is vehicle requirement,
    it is display in account requirement component WOTD-84729
    """
    itemsCache = dependency.descriptor(IItemsCache)

    @classmethod
    def format(cls, condition, event, styler):
        style = styler(condition.isAvailable())
        key = '#quests:details/requirements/vehicle/%s' % ('receivedMultXp' if condition.getValue() else 'notReceivedMultXp')
        label = ms(key, mult=cls.itemsCache.items.shop.dailyXPFactor)
        return [packText(style(label))]


class AccountDossierRequirementFormatter(ConditionFormatter):

    @classmethod
    def format(cls, condition, event, styler):
        style = styler(condition.isAvailable())
        if condition.average:
            titleKey = '#quests:details/requirements/dossierAvgValue'
        else:
            titleKey = '#quests:details/requirements/dossierValue'
        block, record = condition.recordName
        battleMode = cls._dossierBlock2BattleMode(block)
        labelKey = '#quests:details/dossier/{}/{}'.format(battleMode, record)
        label = ms(titleKey, label=ms(labelKey))
        label = relate(condition.relation, condition.relationValue, label)
        return [packText(style(label))]

    @classmethod
    def _dossierBlock2BattleMode(cls, block):
        if block in ('a15x15', 'a15x15_2'):
            return 'random'
        if block in ('company', 'company2'):
            return 'company'
        if block in ('clan', 'clan2'):
            return 'clan'
        if block == 'a7x7':
            return 'team'
        if block == 'rated7x7':
            return 'ladder'
        if block == 'historical':
            return 'historical'
        if block == 'achievements':
            return 'achievements'
        return 'random'


class TokenGatheringRequirementFormatter(ConditionFormatter):
    """ Gathers all token conditions of the group in the single 'condition'.
    """
    eventsCache = dependency.descriptor(IEventsCache)

    def __init__(self):
        self._tokens = []
        self._isAvailable = True

    def format(self, styler):
        style = styler(self._isAvailable)
        result = []
        if self._tokens:
            result = [packText(style('#quests:details/requirements/token')), packTokens(self._tokens)]
        return result

    def gather(self, condition, event):
        if not condition.isDisplayable():
            return
        if event.getType() not in EVENT_TYPE.LIKE_BATTLE_QUESTS + EVENT_TYPE.LIKE_TOKEN_QUESTS:
            return
        needCount = condition.getNeededCount()
        gotCount = condition.getReceivedCount()
        image = condition.getImage(TOKEN_SIZES.BIG)
        self._tokens.append(packTokenProgress(condition.getID(), event.getID(), '', image, gotCount, needCount, isBigSize=True))
        self._isAvailable = self._isAvailable and condition.isAvailable()

    def isAvailable(self):
        return self._isAvailable
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\missions\conditions_formatters\requirements.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:47:14 St�edn� Evropa (letn� �as)
