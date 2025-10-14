import unittest as ut
from main import MySortedDict

class TestMySortedDict(ut.TestCase):
    def setUp(self):
        self.myDict: MySortedDict[str, int] = MySortedDict()
        self.myDict['a'] = 1
        self.myDict['b'] = 2
        self.emptyDict: MySortedDict[str, int] = MySortedDict()
    def test_get_item(self):
        self.assertEqual(2, self.myDict['b'])
        self.assertRaises(KeyError, lambda: self.myDict['c'])
        self.assertRaises(KeyError, lambda: self.emptyDict['a'])
    def test_set_item(self):
        self.myDict['c'] = 3
        self.assertEqual(3, self.myDict['c'])
        self.myDict['a'] = 10
        self.assertEqual(10, self.myDict['a'])
    def test_len(self):
        self.assertEqual(2, len(self.myDict))
        self.assertEqual(0, len(self.emptyDict))
    def test_get(self):
        self.assertEqual(1, self.myDict.get('a'))
        self.assertEqual(None, self.myDict.get('c'))
        self.assertEqual(10, self.myDict.get('c', 10))
        self.assertEqual(None, self.emptyDict.get('a'))
        self.assertEqual(1, self.emptyDict.get('a', 1))
    def test_set_default(self):
        self.assertEqual(1, self.myDict.setdefault('a', 10))
        self.assertEqual(1, self.myDict['a'])
        self.assertEqual(10, self.myDict.setdefault('c', 10))
        self.assertEqual(10, self.myDict['c'])
    def test_keys(self):
        my_keys: list[str] = self.myDict.keys()
        self.assertTrue('a' in my_keys and 'b' in my_keys and len(my_keys) == 2)
        self.assertEqual(0, len(self.emptyDict.keys()))
    def test_items(self):
        my_items: list[tuple[str, int]] = self.myDict.items()
        self.assertTrue(('a', 1) in my_items and ('b', 2) in my_items and len(my_items) == 2)
        self.assertEqual(0, len(self.emptyDict.items()))
    def test_values(self):
        my_values: list[int] = self.myDict.values()
        self.assertTrue(1 in my_values and 2 in my_values and len(my_values) == 2)
        self.assertEqual(0, len(self.emptyDict.values()))
    def test_update(self):
        self.myDict.update('a', 8)
        self.assertEqual(8, self.myDict['a'])
        self.myDict.update('c', 11)
        self.assertEqual(11, self.myDict['c'])
        self.emptyDict.update('a', 1)
        self.assertEqual(1, self.emptyDict['a'])
    def test_pop(self):
        self.assertEqual(1, self.myDict.pop('a', 10))
        self.assertEqual(2, self.myDict.pop('b'))
        self.assertRaises(KeyError, lambda: self.myDict['a'])
        self.assertEqual(2, self.myDict.pop('a', 2))
        self.assertRaises(KeyError, lambda: self.myDict.pop('a'))
    def test_bisect_left(self):
        self.assertEqual(0, self.myDict.bisect_left('a'))
        self.assertEqual(1, self.myDict.bisect_left('b'))
        self.assertEqual(1, self.myDict.bisect_left('aaa'))
        self.assertEqual(2, self.myDict.bisect_left('p'))

        self.assertEqual(0, self.emptyDict.bisect_left('a'))

    def test_bisect_right(self):
        self.assertEqual(1, self.myDict.bisect_right('a'))
        self.assertEqual(2, self.myDict.bisect_right('b'))
        self.assertEqual(1, self.myDict.bisect_right('aaa'))
        self.assertEqual(2, self.myDict.bisect_right('p'))

        self.assertEqual(0, self.emptyDict.bisect_right('a'))

    def test_peek_item(self):
        self.assertRaises(IndexError, self.emptyDict.peekitem, 0)
        self.assertRaises(IndexError, self.emptyDict.peekitem, -1)

        self.assertRaises(IndexError, self.myDict.peekitem, 100)
        self.assertRaises(IndexError, self.myDict.peekitem, -3)

        self.assertEqual(('a', 1), self.myDict.peekitem(0))
        self.assertEqual(('b', 2), self.myDict.peekitem(1))
        self.assertEqual(('b', 2), self.myDict.peekitem(-1))
        self.assertEqual(('a', 1), self.myDict.peekitem(-2))


