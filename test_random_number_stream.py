from typing import Callable
import itertools as it
import unittest as ut
from random_number_stream import RandomNumbersStream

class TestRandomNumberStream(ut.TestCase):
    def setUp(self):
        self.stream: RandomNumbersStream = RandomNumbersStream(min=10, max=100)
        self.test_limit = 2718
        self.is_10_to_100 = lambda p: 10 <= p <= 100
        self.is_even = lambda p: p % 2 == 0

    def __check_condition(self, condition: Callable[[int], bool]):
        self.assertTrue( all(condition(v) for v in it.islice(self.stream, self.test_limit)) )

    def test_unlimited_streaming(self):
        self.__check_condition(self.is_10_to_100)
    
    def test_unlimited_streaming_with_predicate(self):
        self.stream.setFilter(self.is_even)
        self.__check_condition(lambda p: self.is_10_to_100(p) and self.is_even(p))

    def test_limited_streaming_with_predicate(self):
        self.stream.setFilter(self.is_even)
        self.stream.setLimit(10)
        self.__check_condition(lambda p: self.is_10_to_100(p) and self.is_even(p))
        values: list[int] = [x for x in it.islice(self.stream, self.test_limit)]
        self.assertEqual(10, len(values))

if __name__ == "__main__":
    ut.main()