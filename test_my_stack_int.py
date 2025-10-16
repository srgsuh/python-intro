import unittest as ut

from main import MyStackInt


class TestMyStackInt(ut.TestCase):
    def setUp(self):
        self.stack = MyStackInt()
        self.stack.push(2)
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(4)

        self.empty = MyStackInt()

    def test_pop(self):
        self.assertEqual(self.stack.pop(), 4)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.pop(), 2)
        self.assertRaises(IndexError, self.stack.pop)

    def test_max(self):
        self.assertEqual(self.stack.max(), 4)

    def test_max_raises_when_empty(self):
        self.assertRaises(IndexError, self.empty.max)

    def test_push_of_a_bigger_value(self):
        self.stack.push(100)
        self.assertEqual(self.stack.max(), 100)

    def test_push_of_a_smaller_value(self):
        self.stack.push(1)
        self.stack.push(-100)
        self.assertEqual(self.stack.max(), 4)

    def test_pop_of_a_max(self):
        self.stack.pop()
        self.assertEqual(self.stack.max(), 2)

    def test_pop_of_a_duplicate_max(self):
        self.stack.pop()
        self.stack.pop()
        self.assertEqual(self.stack.max(), 2)

if __name__ == '__main__':
    ut.main()
