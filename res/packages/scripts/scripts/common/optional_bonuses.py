# 2017.08.29 21:52:39 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/optional_bonuses.py
import random
import copy
from constants import EVENT_TYPE
from items import tankmen

def walkBonuses(bonusWithProbabilities, visitor):
    result = visitor.resultHolder(bonusWithProbabilities)
    for bonusName, bonusValue in bonusWithProbabilities.iteritems():
        if bonusName == 'oneof':
            deeper = visitor.onOneOf(result, bonusValue)
        elif bonusName == 'allof':
            deeper = visitor.onAllOf(result, bonusValue)
        elif bonusName == 'groups':
            deeper = visitor.onGroup(bonusValue)
        else:
            visitor.onValue(result, bonusName, bonusValue)
            continue
        for bonus in deeper:
            for name, value in walkBonuses(bonus, visitor).iteritems():
                visitor.onMerge(result, name, value)

    return result


def _packTrack(track):
    result = []
    if not track:
        return None
    else:
        curByte = curPos = 0
        for flag in track:
            if flag:
                curByte |= 1 << curPos
            curPos += 1
            if curPos > 7:
                result.append(curByte)
                curByte = curPos = 0

        result.append(curByte)
        result = ''.join(('{:02x}'.format(x) for x in bytearray(result)))
        return result


def _trackIterator(packedTrack):
    for curByte in bytearray.fromhex(packedTrack):
        for i in xrange(8):
            result = bool(curByte & 1 << i)
            yield result


def __mergeValue(total, key, value, isLeaf = False, count = 1, *args):
    total[key] = total.get(key, 0) + count * value


def __mergeFactor(total, key, value, isLeaf, count = 1, *args):
    if isLeaf:
        total[key] = total.get(key, 0) + count * (max(value, 1) - 1)
    else:
        total[key] = total.get(key, 0) + count * value


def __mergeItems(total, key, value, isLeaf = False, count = 1, *args):
    items = total.setdefault(key, {})
    for itemCompDescr, itemCount in value.iteritems():
        items[itemCompDescr] = items.get(itemCompDescr, 0) + count * itemCount


def __mergeVehicles(total, key, value, isLeaf = False, *args):
    vehs = total.setdefault(key, [])
    vehs.extend(value if isinstance(value, list) else [value])


def __mergeTankmen(total, key, value, isLeaf = False, *args):
    tman = total.setdefault(key, [])
    tman.extend(value if isinstance(value, list) else [value])


def __mergeCustomizations(total, key, value, isLeaf, count, vehTypeCompDescr):
    customizations = total.setdefault(key, [])
    for subvalue in value:
        if 'boundToCurrentVehicle' in subvalue:
            subvalue = copy.deepcopy(subvalue)
            subvalue['vehTypeCompDescr'] = vehTypeCompDescr
        customizations.append(subvalue)


def __mergeTokens(total, key, value, isLeaf = False, count = 1, *args):
    totalTokens = total.setdefault(key, {})
    for tokenID, tokenData in value.iteritems():
        total = totalTokens.setdefault(tokenID, {'count': 0,
         'expires': {},
         'limit': 0})
        total['count'] += count * tokenData.get('count', 1)
        if not total['expires']:
            total['expires'] = tokenData['expires']
        if 'limit' in tokenData:
            total['limit'] = tokenData['limit'] if total['limit'] == 0 else max(total['limit'], tokenData['limit'])


def __mergeGoodies(total, key, value, isLeaf = False, count = 1, *args):
    totalGoodies = total.setdefault(key, {})
    for goodieID, goodieData in value.iteritems():
        total = totalGoodies.setdefault(goodieID, {'count': 0,
         'expires': {},
         'limit': 0})
        total['count'] += count * goodieData.get('count', 1)
        if not total['expires'] and 'expires' in goodieData:
            total['expires'] = goodieData['expires']
        if 'limit' in goodieData:
            total['limit'] = goodieData['limit'] if total['limit'] == 0 else max(total['limit'], goodieData['limit'])


def __mergeDossier(total, key, value, isLeaf = False, count = 1, *args):
    totalDossiers = total.setdefault(key, {})
    for _dossierType, changes in value.iteritems():
        totalDossier = totalDossiers.setdefault(_dossierType, {})
        for record, data in changes.iteritems():
            total = totalDossier.setdefault(record, {'value': 0,
             'unique': False,
             'type': 'add'})
            total['value'] += data['value'] * count
            total['unique'] = data['unique']
            total['type'] = data['type']


BONUS_MERGERS = {'credits': __mergeValue,
 'gold': __mergeValue,
 'xp': __mergeValue,
 'crystal': __mergeValue,
 'freeXP': __mergeValue,
 'tankmenXP': __mergeValue,
 'creditsFactor': __mergeFactor,
 'xpFactor': __mergeFactor,
 'freeXPFactor': __mergeFactor,
 'tankmenXPFactor': __mergeFactor,
 'items': __mergeItems,
 'vehicles': __mergeVehicles,
 'slots': __mergeValue,
 'berths': __mergeValue,
 'premium': __mergeValue,
 'tokens': __mergeTokens,
 'goodies': __mergeGoodies,
 'dossier': __mergeDossier,
 'tankmen': __mergeTankmen,
 'customizations': __mergeCustomizations}

class TrackVisitor(object):

    def __init__(self, mergers, track, *args):
        self.__mergers = mergers
        self.__mergersArgs = args
        self.__track = _trackIterator(track)

    def onOneOf(self, bonus, value):
        for probability, bonusValue in value:
            if next(self.__track):
                return [bonusValue]

        raise Exception('Unreachable code, oneof probability bug %s' % value)

    def onAllOf(self, bonus, value):
        deeper = []
        for probability, bonusValue in value:
            if next(self.__track):
                deeper.append(bonusValue)

        return deeper

    def onGroup(self, value):
        deeper = []
        for bonusValue in value:
            deeper.append(bonusValue)

        return deeper

    def onValue(self, bonus, name, value):
        if name in self.__mergers:
            self.__mergers[name](bonus, name, value, True, *self.__mergersArgs)

    def onMerge(self, bonus, name, value):
        if name in self.__mergers:
            self.__mergers[name](bonus, name, value, False, *self.__mergersArgs)

    @staticmethod
    def resultHolder(result):
        return {}


class ProbabilityVisitor(object):

    def __init__(self, mergers, *args):
        self.__mergers = mergers
        self.__mergersArgs = args
        self.__bonusTrack = []

    def bonusTrack(self):
        return _packTrack(self.__bonusTrack)

    def onOneOf(self, bonus, value):
        rand = random.random()
        for probability, bonusValue in value:
            if probability > rand:
                self.__trackChoice(True)
                return [bonusValue]
            self.__trackChoice(False)

        raise Exception('Unreachable code, oneof probability bug %s' % value)

    def onAllOf(self, bonus, value):
        deeper = []
        for probability, bonusValue in value:
            if probability > random.random():
                self.__trackChoice(True)
                deeper.append(bonusValue)
            else:
                self.__trackChoice(False)

        return deeper

    def onGroup(self, value):
        deeper = []
        for bonusValue in value:
            deeper.append(bonusValue)

        return deeper

    def onValue(self, bonus, name, value):
        if name in self.__mergers:
            self.__mergers[name](bonus, name, value, True, *self.__mergersArgs)

    def onMerge(self, bonus, name, value):
        if name in self.__mergers:
            self.__mergers[name](bonus, name, value, False, *self.__mergersArgs)

    def __trackChoice(self, choice):
        self.__bonusTrack.append(choice)

    @staticmethod
    def resultHolder(result):
        return {}


class FilterVisitor(object):

    def __init__(self, eventType = None):
        self.__eventType = eventType

    def onOneOf(self, bonus, value):
        deeper = []
        for probability, bonusValue in value:
            deeper.append(bonusValue)

        return deeper

    def onAllOf(self, bonus, value):
        deeper = []
        for probability, bonusValue in value:
            deeper.append(bonusValue)

        return deeper

    def onGroup(self, value):
        deeper = []
        for bonusValue in value:
            deeper.append(bonusValue)

        return deeper

    def onValue(self, bonus, name, value):
        if self.__eventType != EVENT_TYPE.POTAPOV_QUEST and name == 'tankmen':
            tankmenList = [ tankmen.makeTmanDescrByTmanData(tmanData) for tmanData in value ]
            bonus['tankmen'] = tankmenList
        if self.__eventType in EVENT_TYPE.LIKE_TOKEN_QUESTS and name == 'customization':
            if 'boundToCurrentVehicle' in value:
                raise Exception("Unsupported tag 'boundToCurrentVehicle' in 'like token' quests")

    def onMerge(self, bonus, name, value):
        pass

    @staticmethod
    def resultHolder(result):
        return result


class StripVisitor(object):

    def onOneOf(self, bonus, value):
        result = []
        deeper = []
        for probability, bonusValue in value:
            result.append((-1, bonusValue))
            deeper.append(bonusValue)

        bonus['oneof'] = result
        return deeper

    def onAllOf(self, bonus, value):
        result = []
        deeper = []
        for probability, bonusValue in value:
            result.append((-1, bonusValue))
            deeper.append(bonusValue)

        bonus['allof'] = result
        return deeper

    def onGroup(self, value):
        deeper = []
        for bonusValue in value:
            deeper.append(bonusValue)

        return deeper

    def onValue(self, bonus, name, value):
        pass

    def onMerge(self, bonus, name, value):
        pass

    @staticmethod
    def resultHolder(result):
        return result
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\optional_bonuses.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:52:39 St�edn� Evropa (letn� �as)
