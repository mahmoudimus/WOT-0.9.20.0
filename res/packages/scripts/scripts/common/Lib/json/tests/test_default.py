# 2017.08.29 21:57:15 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/json/tests/test_default.py
from json.tests import PyTest, CTest

class TestDefault(object):

    def test_default(self):
        self.assertEqual(self.dumps(type, default=repr), self.dumps(repr(type)))


class TestPyDefault(TestDefault, PyTest):
    pass


class TestCDefault(TestDefault, CTest):
    pass
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\json\tests\test_default.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:57:15 St�edn� Evropa (letn� �as)
