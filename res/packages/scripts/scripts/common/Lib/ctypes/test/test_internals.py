# 2017.08.29 21:55:46 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/ctypes/test/test_internals.py
import unittest
from ctypes import *
from sys import getrefcount as grc

class ObjectsTestCase(unittest.TestCase):

    def assertSame(self, a, b):
        self.assertEqual(id(a), id(b))

    def test_ints(self):
        i = 42000123
        refcnt = grc(i)
        ci = c_int(i)
        self.assertEqual(refcnt, grc(i))
        self.assertEqual(ci._objects, None)
        return

    def test_c_char_p(self):
        s = 'Hello, World'
        refcnt = grc(s)
        cs = c_char_p(s)
        self.assertEqual(refcnt + 1, grc(s))
        self.assertSame(cs._objects, s)

    def test_simple_struct(self):

        class X(Structure):
            _fields_ = [('a', c_int), ('b', c_int)]

        a = 421234
        b = 421235
        x = X()
        self.assertEqual(x._objects, None)
        x.a = a
        x.b = b
        self.assertEqual(x._objects, None)
        return

    def test_embedded_structs(self):

        class X(Structure):
            _fields_ = [('a', c_int), ('b', c_int)]

        class Y(Structure):
            _fields_ = [('x', X), ('y', X)]

        y = Y()
        self.assertEqual(y._objects, None)
        x1, x2 = X(), X()
        y.x, y.y = x1, x2
        self.assertEqual(y._objects, {'0': {},
         '1': {}})
        x1.a, x2.b = (42, 93)
        self.assertEqual(y._objects, {'0': {},
         '1': {}})
        return

    def test_xxx(self):

        class X(Structure):
            _fields_ = [('a', c_char_p), ('b', c_char_p)]

        class Y(Structure):
            _fields_ = [('x', X), ('y', X)]

        s1 = 'Hello, World'
        s2 = 'Hallo, Welt'
        x = X()
        x.a = s1
        x.b = s2
        self.assertEqual(x._objects, {'0': s1,
         '1': s2})
        y = Y()
        y.x = x
        self.assertEqual(y._objects, {'0': {'0': s1,
               '1': s2}})

    def test_ptr_struct(self):

        class X(Structure):
            _fields_ = [('data', POINTER(c_int))]

        A = c_int * 4
        a = A(11, 22, 33, 44)
        self.assertEqual(a._objects, None)
        x = X()
        x.data = a
        return


if __name__ == '__main__':
    unittest.main()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\ctypes\test\test_internals.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:55:46 St�edn� Evropa (letn� �as)