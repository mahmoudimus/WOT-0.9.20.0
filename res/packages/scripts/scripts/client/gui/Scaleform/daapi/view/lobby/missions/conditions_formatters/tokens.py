# 2017.08.29 21:47:14 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/missions/conditions_formatters/tokens.py
from collections import namedtuple
from gui.server_events.cond_formatters.formatters import ConditionFormatter, ConditionsFormatter
from gui.server_events.formatters import TOKEN_SIZES
from gui.shared.formatters import text_styles
from helpers import dependency
from skeletons.gui.server_events import IEventsCache
_PreFormattedTokenCondition = namedtuple('_PreFormattedTokenCondition', 'tokenID, styleID, eventID, needCount')

class PreFormattedTokenCondition(_PreFormattedTokenCondition):
    eventsCache = dependency.descriptor(IEventsCache)

    @property
    def gotCount(self):
        return self.eventsCache.questsProgress.getTokenCount(self.tokenID)

    @property
    def title(self):
        title = self.eventsCache.prefetcher.getTokenInfo(self.styleID)
        return title

    def getCounterText(self):
        if self.gotCount == self.needCount:
            tokensGot = text_styles.bonusAppliedText(self.gotCount)
        else:
            tokensGot = text_styles.stats(self.gotCount)
        tokensNeed = text_styles.standard(self.needCount)
        return text_styles.disabled('{} / {}'.format(tokensGot, tokensNeed))

    def getImage(self, size):
        return self.eventsCache.prefetcher.getTokenImage(self.styleID, size)


class TokenConditionFormatter(ConditionFormatter):

    def format(self, condition, event):
        needCount = condition.getNeededCount()
        styleID = condition.getStyleID()
        tokenId = condition.getID()
        return [PreFormattedTokenCondition(tokenId, styleID, event.getID(), needCount)]


class TokensConditionFormatter(ConditionsFormatter):

    def __init__(self):
        super(TokensConditionFormatter, self).__init__({'token': TokenConditionFormatter()})

    def format(self, conditions, event):
        result = []
        tokenConditions = conditions.getTokens()
        for condition in tokenConditions:
            if condition.isDisplayable():
                fmt = self.getConditionFormatter(condition.getName())
                result.extend(fmt.format(condition, event))

        return result


class TokensMarathonFormatter(object):
    """ This is a special formatter for the marathon header.
    
    In the marathon header we display visualized tokens, i.e. images of
    tokens fetched from web.
    """
    BIG_ICONS_COUNT = 2

    def __init__(self):
        self.__tokensConditionsFormatter = TokensConditionFormatter()

    def format(self, event):
        result = []
        preFormattedTokenConditions = self.__tokensConditionsFormatter.format(event.accountReqs, event)
        isNormalSize = len(preFormattedTokenConditions) > self.BIG_ICONS_COUNT
        size = TOKEN_SIZES.MEDIUM if isNormalSize else TOKEN_SIZES.BIG
        for preFormattedCondition in preFormattedTokenConditions:
            result.append({'tokenId': preFormattedCondition.tokenID,
             'questId': preFormattedCondition.eventID,
             'isNormalSize': isNormalSize,
             'imgSrc': preFormattedCondition.getImage(size),
             'countText': preFormattedCondition.getCounterText()})

        return result
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\Scaleform\daapi\view\lobby\missions\conditions_formatters\tokens.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:47:14 St�edn� Evropa (letn� �as)
