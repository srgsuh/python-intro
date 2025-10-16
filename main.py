from typing import Callable, Iterator, Iterable
from sortedcontainers import SortedList


def _merge_interval(intervals: list[tuple[int, int]], left: int, right: int)->None:
    if intervals and intervals[-1][1] == left:
        intervals[-1][1] = right
    else:
        intervals.append((left, right))


class NumberBox:
    #TODO constructor defining most effective data structure
    def __init__(self, iterable: Iterable[int] = None):
        self.numbers = SortedList(iterable)

    def addNumber(self, num: int):
        """Add a number to the NumberBox. Time complexity is O(log n)"""
        #TODO adds number
        self.numbers.add(num)

    def removeNumber(self,num: int)->int:
        """Remove one occurrence of a number from the NumberBox. Time complexity is O(log n)"""
        #TODO removes first occurrence of number and returns removed number or None if number missing
        value = None
        if num in self.numbers:
            self.numbers.remove(num)
            value = num
        return value

    def _value_range(self, value: int) -> tuple[int, int]:
        return self.numbers.bisect_left(value), self.numbers.bisect_right(value)

    def removeNumbersPredicate(self,pred: Callable[[int], bool])->int:
        """Removes all numbers matching a given predicate from the NumberBox.
        Time complexity is O(n*log(n))"""
        #TODO removes all numbers matching a given predicate
        #predicate - function taking integer and returning True if the integer matches the predicate otherwise False
        #returns count of the removed numbers
        intervals: list[tuple[int, int]] = []
        visited: set[int] = set()

        for value in self.numbers:
            if value not in visited and pred(value):
                left, right = self._value_range(value)
                _merge_interval(intervals, left, right)

        for left, right in intervals.reverse():
            del self.numbers[left:right]

    def removeNumbersRange(self, minValue: int, maxValue: int)->int:
        """Removes all numbers from the NumberBox that are >=min and <=max. Time complexity is O(log n)"""
        #TODO removes all numbers that >=min and <=max
        #returns count of removed numbers
        left = self.numbers.bisect_left(minValue)
        right = self.numbers.bisect_right(maxValue)
        if left < right:
            del self.numbers[left:right]
        return max(0, right - left)

    def __iter__(self) -> Iterator[int]:
        #TODO code for ierating all numbers from NumberBox instance
        return iter(self.numbers)

    def distinct(self)->int:
        #TODO removing repeated numbers
        raise NotImplementedError()