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


