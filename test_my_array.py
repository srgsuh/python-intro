import unittest as ut
from main import MyArray

class TestMyArray(ut.TestCase):
    def setUp(self):
        self.array: MyArray[int] = MyArray(1_000_000)
        self.array.setAll(1)
        self.array.set(0, 0)
        self.array.set(99_999, 9)
        self.empty: MyArray[int] = MyArray(10)

    def test_get_raise_when_index_out_of_range(self):
        self.assertRaises(IndexError, self.array.get, -1)
        self.assertRaises(IndexError, self.array.get, 1_000_000)

    def test_get_raise_when_value_is_not_set(self):
        self.assertRaises(IndexError, self.empty.get, 1)

    def test_set_raise_when_index_out_of_range(self):
        self.assertRaises(IndexError, self.array.set, -1, 1)
        self.assertRaises(IndexError, self.array.set, 1_000_000, 1)

    def test_get(self):
        self.assertEqual(self.array.get(0), 0)
        self.assertEqual(self.array.get(99_999), 9)
        self.assertEqual(self.array.get(900_000), 1)

    def test_set(self):
        self.array.set(0, -1)
        self.assertEqual(self.array.get(0), -1)
        self.array.set(99_999, 2)
        self.assertEqual(self.array.get(99_999), 2)
        self.array.set(999_999, 99)
        self.assertEqual(self.array.get(999_999), 99)

    def test_setAll(self):
        self.array.setAll(-1)
        values = [self.array.get(x) for x in [0, 1, 3, 1_000, 100_000, 99_999, 999_999]]
        self.assertEqual(values, [-1] * 7)

