# 2017.08.29 21:59:05 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/common/Lib/sqlite3/test/types.py
import datetime
import unittest
import sqlite3 as sqlite
try:
    import zlib
except ImportError:
    zlib = None

class SqliteTypeTests(unittest.TestCase):

    def setUp(self):
        self.con = sqlite.connect(':memory:')
        self.cur = self.con.cursor()
        self.cur.execute('create table test(i integer, s varchar, f number, b blob)')

    def tearDown(self):
        self.cur.close()
        self.con.close()

    def CheckString(self):
        self.cur.execute('insert into test(s) values (?)', (u'\xd6sterreich',))
        self.cur.execute('select s from test')
        row = self.cur.fetchone()
        self.assertEqual(row[0], u'\xd6sterreich')

    def CheckSmallInt(self):
        self.cur.execute('insert into test(i) values (?)', (42,))
        self.cur.execute('select i from test')
        row = self.cur.fetchone()
        self.assertEqual(row[0], 42)

    def CheckLargeInt(self):
        num = 1099511627776L
        self.cur.execute('insert into test(i) values (?)', (num,))
        self.cur.execute('select i from test')
        row = self.cur.fetchone()
        self.assertEqual(row[0], num)

    def CheckFloat(self):
        val = 3.14
        self.cur.execute('insert into test(f) values (?)', (val,))
        self.cur.execute('select f from test')
        row = self.cur.fetchone()
        self.assertEqual(row[0], val)

    def CheckBlob(self):
        val = buffer('Guglhupf')
        self.cur.execute('insert into test(b) values (?)', (val,))
        self.cur.execute('select b from test')
        row = self.cur.fetchone()
        self.assertEqual(row[0], val)

    def CheckUnicodeExecute(self):
        self.cur.execute(u"select '\xd6sterreich'")
        row = self.cur.fetchone()
        self.assertEqual(row[0], u'\xd6sterreich')

    def CheckNonUtf8_Default(self):
        try:
            self.cur.execute('select ?', (chr(150),))
            self.fail('should have raised a ProgrammingError')
        except sqlite.ProgrammingError:
            pass

    def CheckNonUtf8_TextFactoryString(self):
        orig_text_factory = self.con.text_factory
        try:
            self.con.text_factory = str
            self.cur.execute('select ?', (chr(150),))
        finally:
            self.con.text_factory = orig_text_factory

    def CheckNonUtf8_TextFactoryOptimizedUnicode(self):
        orig_text_factory = self.con.text_factory
        try:
            self.con.text_factory = sqlite.OptimizedUnicode
            self.cur.execute('select ?', (chr(150),))
            self.fail('should have raised a ProgrammingError')
        except sqlite.ProgrammingError:
            pass
        finally:
            self.con.text_factory = orig_text_factory


class DeclTypesTests(unittest.TestCase):

    class Foo:

        def __init__(self, _val):
            self.val = _val

        def __cmp__(self, other):
            if not isinstance(other, DeclTypesTests.Foo):
                raise ValueError
            if self.val == other.val:
                return 0
            else:
                return 1

        def __conform__(self, protocol):
            if protocol is sqlite.PrepareProtocol:
                return self.val
            else:
                return None
                return None

        def __str__(self):
            return '<%s>' % self.val

    def setUp(self):
        self.con = sqlite.connect(':memory:', detect_types=sqlite.PARSE_DECLTYPES)
        self.cur = self.con.cursor()
        self.cur.execute('create table test(i int, s str, f float, b bool, u unicode, foo foo, bin blob, n1 number, n2 number(5))')
        sqlite.converters['FLOAT'] = lambda x: 47.2
        sqlite.converters['BOOL'] = lambda x: bool(int(x))
        sqlite.converters['FOO'] = DeclTypesTests.Foo
        sqlite.converters['WRONG'] = lambda x: 'WRONG'
        sqlite.converters['NUMBER'] = float

    def tearDown(self):
        del sqlite.converters['FLOAT']
        del sqlite.converters['BOOL']
        del sqlite.converters['FOO']
        del sqlite.converters['NUMBER']
        self.cur.close()
        self.con.close()

    def CheckString(self):
        self.cur.execute('insert into test(s) values (?)', ('foo',))
        self.cur.execute('select s as "s [WRONG]" from test')
        row = self.cur.fetchone()
        self.assertEqual(row[0], 'foo')

    def CheckSmallInt(self):
        self.cur.execute('insert into test(i) values (?)', (42,))
        self.cur.execute('select i from test')
        row = self.cur.fetchone()
        self.assertEqual(row[0], 42)

    def CheckLargeInt(self):
        num = 1099511627776L
        self.cur.execute('insert into test(i) values (?)', (num,))
        self.cur.execute('select i from test')
        row = self.cur.fetchone()
        self.assertEqual(row[0], num)

    def CheckFloat(self):
        val = 3.14
        self.cur.execute('insert into test(f) values (?)', (val,))
        self.cur.execute('select f from test')
        row = self.cur.fetchone()
        self.assertEqual(row[0], 47.2)

    def CheckBool(self):
        self.cur.execute('insert into test(b) values (?)', (False,))
        self.cur.execute('select b from test')
        row = self.cur.fetchone()
        self.assertEqual(row[0], False)
        self.cur.execute('delete from test')
        self.cur.execute('insert into test(b) values (?)', (True,))
        self.cur.execute('select b from test')
        row = self.cur.fetchone()
        self.assertEqual(row[0], True)

    def CheckUnicode(self):
        val = u'\xd6sterreich'
        self.cur.execute('insert into test(u) values (?)', (val,))
        self.cur.execute('select u from test')
        row = self.cur.fetchone()
        self.assertEqual(row[0], val)

    def CheckFoo(self):
        val = DeclTypesTests.Foo('bla')
        self.cur.execute('insert into test(foo) values (?)', (val,))
        self.cur.execute('select foo from test')
        row = self.cur.fetchone()
        self.assertEqual(row[0], val)

    def CheckUnsupportedSeq(self):

        class Bar:
            pass

        val = Bar()
        try:
            self.cur.execute('insert into test(f) values (?)', (val,))
            self.fail('should have raised an InterfaceError')
        except sqlite.InterfaceError:
            pass
        except:
            self.fail('should have raised an InterfaceError')

    def CheckUnsupportedDict(self):

        class Bar:
            pass

        val = Bar()
        try:
            self.cur.execute('insert into test(f) values (:val)', {'val': val})
            self.fail('should have raised an InterfaceError')
        except sqlite.InterfaceError:
            pass
        except:
            self.fail('should have raised an InterfaceError')

    def CheckBlob(self):
        val = buffer('Guglhupf')
        self.cur.execute('insert into test(bin) values (?)', (val,))
        self.cur.execute('select bin from test')
        row = self.cur.fetchone()
        self.assertEqual(row[0], val)

    def CheckNumber1(self):
        self.cur.execute('insert into test(n1) values (5)')
        value = self.cur.execute('select n1 from test').fetchone()[0]
        self.assertEqual(type(value), float)

    def CheckNumber2(self):
        """Checks whether converter names are cut off at '(' characters"""
        self.cur.execute('insert into test(n2) values (5)')
        value = self.cur.execute('select n2 from test').fetchone()[0]
        self.assertEqual(type(value), float)


class ColNamesTests(unittest.TestCase):

    def setUp(self):
        self.con = sqlite.connect(':memory:', detect_types=sqlite.PARSE_COLNAMES)
        self.cur = self.con.cursor()
        self.cur.execute('create table test(x foo)')
        sqlite.converters['FOO'] = lambda x: '[%s]' % x
        sqlite.converters['BAR'] = lambda x: '<%s>' % x
        sqlite.converters['EXC'] = lambda x: 5 // 0
        sqlite.converters['B1B1'] = lambda x: 'MARKER'

    def tearDown(self):
        del sqlite.converters['FOO']
        del sqlite.converters['BAR']
        del sqlite.converters['EXC']
        del sqlite.converters['B1B1']
        self.cur.close()
        self.con.close()

    def CheckDeclTypeNotUsed(self):
        """
        Assures that the declared type is not used when PARSE_DECLTYPES
        is not set.
        """
        self.cur.execute('insert into test(x) values (?)', ('xxx',))
        self.cur.execute('select x from test')
        val = self.cur.fetchone()[0]
        self.assertEqual(val, 'xxx')

    def CheckNone(self):
        self.cur.execute('insert into test(x) values (?)', (None,))
        self.cur.execute('select x from test')
        val = self.cur.fetchone()[0]
        self.assertEqual(val, None)
        return

    def CheckColName(self):
        self.cur.execute('insert into test(x) values (?)', ('xxx',))
        self.cur.execute('select x as "x [bar]" from test')
        val = self.cur.fetchone()[0]
        self.assertEqual(val, '<xxx>')
        self.assertEqual(self.cur.description[0][0], 'x')

    def CheckCaseInConverterName(self):
        self.cur.execute('select \'other\' as "x [b1b1]"')
        val = self.cur.fetchone()[0]
        self.assertEqual(val, 'MARKER')

    def CheckCursorDescriptionNoRow(self):
        """
        cursor.description should at least provide the column name(s), even if
        no row returned.
        """
        self.cur.execute('select * from test where 0 = 1')
        self.assertEqual(self.cur.description[0][0], 'x')


class ObjectAdaptationTests(unittest.TestCase):

    def cast(obj):
        return float(obj)

    cast = staticmethod(cast)

    def setUp(self):
        self.con = sqlite.connect(':memory:')
        try:
            del sqlite.adapters[int]
        except:
            pass

        sqlite.register_adapter(int, ObjectAdaptationTests.cast)
        self.cur = self.con.cursor()

    def tearDown(self):
        del sqlite.adapters[int, sqlite.PrepareProtocol]
        self.cur.close()
        self.con.close()

    def CheckCasterIsUsed(self):
        self.cur.execute('select ?', (4,))
        val = self.cur.fetchone()[0]
        self.assertEqual(type(val), float)


@unittest.skipUnless(zlib, 'requires zlib')

class BinaryConverterTests(unittest.TestCase):

    def convert(s):
        return zlib.decompress(s)

    convert = staticmethod(convert)

    def setUp(self):
        self.con = sqlite.connect(':memory:', detect_types=sqlite.PARSE_COLNAMES)
        sqlite.register_converter('bin', BinaryConverterTests.convert)

    def tearDown(self):
        self.con.close()

    def CheckBinaryInputForConverter(self):
        testdata = 'abcdefg' * 10
        result = self.con.execute('select ? as "x [bin]"', (buffer(zlib.compress(testdata)),)).fetchone()[0]
        self.assertEqual(testdata, result)


class DateTimeTests(unittest.TestCase):

    def setUp(self):
        self.con = sqlite.connect(':memory:', detect_types=sqlite.PARSE_DECLTYPES)
        self.cur = self.con.cursor()
        self.cur.execute('create table test(d date, ts timestamp)')

    def tearDown(self):
        self.cur.close()
        self.con.close()

    def CheckSqliteDate(self):
        d = sqlite.Date(2004, 2, 14)
        self.cur.execute('insert into test(d) values (?)', (d,))
        self.cur.execute('select d from test')
        d2 = self.cur.fetchone()[0]
        self.assertEqual(d, d2)

    def CheckSqliteTimestamp(self):
        ts = sqlite.Timestamp(2004, 2, 14, 7, 15, 0)
        self.cur.execute('insert into test(ts) values (?)', (ts,))
        self.cur.execute('select ts from test')
        ts2 = self.cur.fetchone()[0]
        self.assertEqual(ts, ts2)

    def CheckSqlTimestamp(self):
        if sqlite.sqlite_version_info < (3, 1):
            return
        now = datetime.datetime.now()
        self.cur.execute('insert into test(ts) values (current_timestamp)')
        self.cur.execute('select ts from test')
        ts = self.cur.fetchone()[0]
        self.assertEqual(type(ts), datetime.datetime)
        self.assertEqual(ts.year, now.year)

    def CheckDateTimeSubSeconds(self):
        ts = sqlite.Timestamp(2004, 2, 14, 7, 15, 0, 500000)
        self.cur.execute('insert into test(ts) values (?)', (ts,))
        self.cur.execute('select ts from test')
        ts2 = self.cur.fetchone()[0]
        self.assertEqual(ts, ts2)

    def CheckDateTimeSubSecondsFloatingPoint(self):
        ts = sqlite.Timestamp(2004, 2, 14, 7, 15, 0, 510241)
        self.cur.execute('insert into test(ts) values (?)', (ts,))
        self.cur.execute('select ts from test')
        ts2 = self.cur.fetchone()[0]
        self.assertEqual(ts, ts2)


def suite():
    sqlite_type_suite = unittest.makeSuite(SqliteTypeTests, 'Check')
    decltypes_type_suite = unittest.makeSuite(DeclTypesTests, 'Check')
    colnames_type_suite = unittest.makeSuite(ColNamesTests, 'Check')
    adaptation_suite = unittest.makeSuite(ObjectAdaptationTests, 'Check')
    bin_suite = unittest.makeSuite(BinaryConverterTests, 'Check')
    date_suite = unittest.makeSuite(DateTimeTests, 'Check')
    return unittest.TestSuite((sqlite_type_suite,
     decltypes_type_suite,
     colnames_type_suite,
     adaptation_suite,
     bin_suite,
     date_suite))


def test():
    runner = unittest.TextTestRunner()
    runner.run(suite())


if __name__ == '__main__':
    test()
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\common\Lib\sqlite3\test\types.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:59:06 St�edn� Evropa (letn� �as)
