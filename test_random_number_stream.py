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
    
    def test_sport_lotto(self):
        numbers = RandomNumbersStream(min=1, max=49)
        numbers.setDistinct()
        numbers.setLimit(10)
        values: list[int] = [x for x in it.islice(numbers, self.test_limit)]
        # Exactly 10 numbers generated
        self.assertEqual(10, len(values)) 
        # All numbers are distinct
        sorted_values = sorted(values)
        sorted_unique = [x for idx, x in enumerate(sorted_values) if idx == 0 or sorted_values[idx] > sorted_values[idx - 1]]
        self.assertEqual(10, len(sorted_unique))
        # All numbers are in the range from 1 to 49
        self.assertTrue(all(x >= 1 and x <= 49 for x in values))

if __name__ == "__main__":
    ut.main()