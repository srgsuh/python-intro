import unittest as ut
from main import MyDict

class TestMyDict(ut.TestCase):
    def setUp(self):
        self.myDict: MyDict[str, int] = MyDict()
        self.myDict['a'] = 1
        self.myDict['b'] = 2
    def test_get_item(self):
        self.assertEqual(2, self.myDict['b'])
    def test_set_item(self):
        self.myDict['c'] = 3
        self.assertEqual(3, self.myDict['c'])
        self.myDict['a'] = 10
        self.assertEqual(10, self.myDict['a'])
    def test_len(self):
        self.assertEqual(2, len(self.myDict))
    def test_get(self):
        self.assertEqual(1, self.myDict.get('a'))
        self.assertEqual(None, self.myDict.get('c'))
        self.assertEqual(10, self.myDict.get('c', 10))
    def test_set_default(self):
        self.assertEqual(1, self.myDict.setdefault('a', 10))
        self.assertEqual(1, self.myDict['a'])
        self.assertEqual(10, self.myDict.setdefault('c', 10))
        self.assertEqual(10, self.myDict['c'])



