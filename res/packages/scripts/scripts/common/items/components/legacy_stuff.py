# 2017.08.29 21:53:26 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/items/components/legacy_stuff.py
from constants import IS_CLIENT, IS_CELLAPP, IS_BASEAPP
_IS_LEGACY_STUFF_SUPPORTED = not IS_CLIENT and not IS_CELLAPP and not IS_BASEAPP

class SupportedLegacyStuff(object):
    """Decorator to make dict-like object, but support is not full."""
    __slots__ = ()

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __contains__(self, item):
        return hasattr(self, item)

    def __iter__(self):
        raise NotImplementedError

    def keys(self):
        raise NotImplementedError

    def values(self):
        raise NotImplementedError

    def items(self):
        raise NotImplementedError

    def get(self, k, d = None):
        return getattr(self, k, d)

    def copy(self):
        raise NotImplementedError

    def clear(self):
        raise NotImplementedError

    def has_key(self, k):
        raise NotImplementedError

    def update(self, *args, **kwargs):
        raise NotImplementedError

    def pop(self, *args):
        raise NotImplementedError


class NoLegacyStuff(object):
    """Decorator to disallow dict-like behavior."""
    __slots__ = ()

    def __getitem__(self, item):
        raise AssertionError('Operation is not allowed')

    def __setitem__(self, key, value):
        raise AssertionError('Operation is not allowed')

    def __contains__(self, item):
        raise AssertionError('Operation is not allowed')

    def __iter__(self):
        raise AssertionError('Operation is not allowed')

    def keys(self):
        raise AssertionError('Operation is not supported')

    def values(self):
        raise AssertionError('Operation is not supported')

    def items(self):
        raise AssertionError('Operation is not supported')

    def get(self, k, d = None):
        raise AssertionError('Operation is not allowed')

    def copy(self):
        raise NotImplementedError

    def clear(self):
        raise AssertionError('Operation is not allowed')

    def has_key(self, k):
        raise AssertionError('Operation is not allowed')

    def update(self, *args, **kwargs):
        raise AssertionError('Operation is not allowed')

    def pop(self, *args):
        raise AssertionError('Operation is not allowed')


if _IS_LEGACY_STUFF_SUPPORTED:
    LegacyStuff = SupportedLegacyStuff
else:
    LegacyStuff = NoLegacyStuff
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\items\components\legacy_stuff.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:53:26 St�edn� Evropa (letn� �as)
