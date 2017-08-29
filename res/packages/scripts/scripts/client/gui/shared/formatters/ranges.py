# 2017.08.29 21:49:33 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/formatters/ranges.py
from helpers import int2roman

def toRangeString(sequence, step, itemDelimiter = ', ', rangeDelimiter = '-'):
    items = list()
    for item in list(stringRanges(sequence, step)):
        items.append(rangeDelimiter.join(item))

    return itemDelimiter.join(items)


def toRomanRangeString(sequence, step, itemDelimiter = ', ', rangeDelimiter = '-'):
    items = list()
    for item in list(romanStringRanges(sequence, step)):
        items.append(rangeDelimiter.join(item))

    return itemDelimiter.join(items)


def stringRanges(sequence, step):
    for item in numberRanges(sequence, step):
        yield map(str, item)


def romanStringRanges(sequence, step):
    for item in numberRanges(sequence, step):
        yield map(int2roman, item)


def numberRanges(sequence, step):
    length = len(sequence)
    if length > 0:
        q = sorted(sequence)
        i = 0
        for j in xrange(1, length):
            if q[j] > step + q[j - 1]:
                if i == j - 1:
                    yield (q[i],)
                else:
                    yield (q[i], q[j - 1])
                i = j

        if i == length - 1:
            yield (q[i],)
        else:
            yield (q[i], q[-1])
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\formatters\ranges.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:49:33 St�edn� Evropa (letn� �as)
