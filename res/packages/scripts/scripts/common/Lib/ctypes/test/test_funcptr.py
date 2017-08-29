# 2017.08.29 21:55:45 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/ctypes/test/test_funcptr.py
import os, unittest
from ctypes import *
try:
    WINFUNCTYPE
except NameError:
    WINFUNCTYPE = CFUNCTYPE

import _ctypes_test
lib = CDLL(_ctypes_test.__file__)

class CFuncPtrTestCase(unittest.TestCase):

    def test_basic(self):
        X = WINFUNCTYPE(c_int, c_int, c_int)

        def func(*args):
            return len(args)

        x = X(func)
        self.assertEqual(x.restype, c_int)
        self.assertEqual(x.argtypes, (c_int, c_int))
        self.assertEqual(sizeof(x), sizeof(c_voidp))
        self.assertEqual(sizeof(X), sizeof(c_voidp))

    def test_first(self):
        StdCallback = WINFUNCTYPE(c_int, c_int, c_int)
        CdeclCallback = CFUNCTYPE(c_int, c_int, c_int)

        def func(a, b):
            return a + b

        s = StdCallback(func)
        c = CdeclCallback(func)
        self.assertEqual(s(1, 2), 3)
        self.assertEqual(c(1, 2), 3)
        self.assertEqual(c(1, 2, 3, 4, 5, 6), 3)
        if WINFUNCTYPE is not CFUNCTYPE and os.name != 'ce':
            self.assertRaises(TypeError, s, 1, 2, 3)

    def test_structures(self):
        WNDPROC = WINFUNCTYPE(c_long, c_int, c_int, c_int, c_int)

        def wndproc(hwnd, msg, wParam, lParam):
            return hwnd + msg + wParam + lParam

        HINSTANCE = c_int
        HICON = c_int
        HCURSOR = c_int
        LPCTSTR = c_char_p

        class WNDCLASS(Structure):
            _fields_ = [('style', c_uint),
             ('lpfnWndProc', WNDPROC),
             ('cbClsExtra', c_int),
             ('cbWndExtra', c_int),
             ('hInstance', HINSTANCE),
             ('hIcon', HICON),
             ('hCursor', HCURSOR),
             ('lpszMenuName', LPCTSTR),
             ('lpszClassName', LPCTSTR)]

        wndclass = WNDCLASS()
        wndclass.lpfnWndProc = WNDPROC(wndproc)
        WNDPROC_2 = WINFUNCTYPE(c_long, c_int, c_int, c_int, c_int)
        self.assertIs(WNDPROC, WNDPROC_2)
        self.assertEqual(wndclass.lpfnWndProc(1, 2, 3, 4), 10)
        f = wndclass.lpfnWndProc
        del wndclass
        del wndproc
        self.assertEqual(f(10, 11, 12, 13), 46)

    def test_dllfunctions(self):

        def NoNullHandle(value):
            if not value:
                raise WinError()
            return value

        strchr = lib.my_strchr
        strchr.restype = c_char_p
        strchr.argtypes = (c_char_p, c_char)
        self.assertEqual(strchr('abcdefghi', 'b'), 'bcdefghi')
        self.assertEqual(strchr('abcdefghi', 'x'), None)
        strtok = lib.my_strtok
        strtok.restype = c_char_p

        def c_string(init):
            size = len(init) + 1
            return (c_char * size)(*init)

        s = 'a\nb\nc'
        b = c_string(s)
        self.assertEqual(strtok(b, '\n'), 'a')
        self.assertEqual(strtok(None, '\n'), 'b')
        self.assertEqual(strtok(None, '\n'), 'c')
        self.assertEqual(strtok(None, '\n'), None)
        return


if __name__ == '__main__':
    unittest.main()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\ctypes\test\test_funcptr.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:55:45 St�edn� Evropa (letn� �as)
