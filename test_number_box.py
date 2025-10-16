import unittest as ut
from main import NumberBox

class TestNumberBox(ut.TestCase):
    def setUp(self):
        self.arr = [1, 1, 2, 2, 2, 3, 4, 4, 4, 5]
        self.box = NumberBox(self.arr.reverse())

    def test_iter(self):
        self.assertEqual(sorted(self.box), self.arr)

    def test_add_number_not_existing(self):
        self.box.addNumber(-100)
        self.assertEqual(sorted(self.box), [-100] + self.arr)

    def test_add_number_existing(self):
        self.box.addNumber(5)
        self.assertEqual(sorted(self.box), self.arr + [5])

    def test_remove_number_not_existing(self):
        self.assertIsNone(self.box.removeNumber(-100))
        self.assertEqual(sorted(self.box), self.arr)

    def test_remove_number_existing(self):
        self.box.removeNumber(5)
        self.assertEqual(sorted(self.box), self.arr[:-1])

    def test_remove_numbers_predicate_partial(self):
        is_even = lambda x: x % 2 == 0
        self.assertEqual(self.box.removeNumbersPredicate(is_even), 6)
        self.assertEqual(sorted(self.box), [1, 1, 3, 5])

    def test_remove_numbers_predicate_all(self):
        is_positive = lambda x: x > 0
        self.assertEqual(self.box.removeNumbersPredicate(is_positive), len(self.arr))
        self.assertEqual(list(self.box), [])

    def test_remove_numbers_range_partial(self):
        self.assertEqual(self.box.removeNumbersRange(2, 4), 3)
        self.assertEqual(sorted(self.box), [1, 1, 5])

    def test_remove_numbers_range_all(self):
        self.assertEqual(self.box.removeNumbersRange(0, 10), len(self.arr))
        self.assertEqual(list(self.box), [])

    def test_remove_numbers_range_empty(self):
        self.assertEqual(self.box.removeNumbersRange(10, 100), 0)
        self.assertEqual(sorted(self.box), self.arr)

    def test_distinct(self):
        self.assertEqual(self.box.distinct(), 5)
        self.assertEqual(sorted(self.box), [1, 2, 3, 4, 5])

