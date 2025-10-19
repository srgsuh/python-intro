from typing import Callable, Iterator, Iterable
from sortedcontainers import SortedList

_last_visited = object()

def _merge_intervals(intervals: list[tuple[int, int]], left: int, right: int)->None:
    """Merge a new interval into a collection of sorted intervals."""
    if intervals and intervals[-1][1] == left:
        intervals[-1] = intervals[-1][0], right
    else:
        intervals.append((left, right))

class NumberBox():
    #TODO constructor defining most effective data structure
    def __init__(self, iterable: Iterable[int] = None):
        self.numbers = SortedList(iterable)

    def addNumber(self, num: int):
        #Time complexity is O(log n)
        #TODO adds number
        self.numbers.add(num)

    def removeNumber(self,num: int)->int:
        #ime complexity is O(log n)
        #TODO removes first occurrence of number and returns removed number or None if number missing
        value = None
        if num in self.numbers:
            self.numbers.remove(num)
            value = num
        return value

    def _index_range(self, min_value: int, max_value: int = None) -> tuple[int, int]:
        return self.numbers.bisect_left(min_value), self.numbers.bisect_right(max_value or min_value)

    def _unique_values(self) -> Iterator[int]:
        last_visited = _last_visited
        for value in self.numbers:
            if value != last_visited:
                last_visited = value
                yield value

    def removeNumbersPredicate(self,pred: Callable[[int], bool])->int:
        #Time complexity is O(n*log(n)). Space complexity is O(n).
        #TODO removes all numbers matching a given predicate
        #predicate - function taking integer and returning True if the integer matches the predicate otherwise False
        #returns count of the removed numbers

        intervals: list[tuple[int, int]] = []
        for value in self._unique_values():
            if pred(value):
                left, right = self._index_range(value, value)
                _merge_intervals(intervals, left, right)

        deleted: int = 0
        for left, right in reversed(intervals):
            deleted += right - left
            del self.numbers[left:right]

        return deleted

    def removeNumbersRange(self, minValue: int, maxValue: int)->int:
        #Time complexity is O(log n). Space complexity is O(1) (if __delitem__ does not consume memory).
        #TODO removes all numbers that >=min and <=max
        #returns count of removed numbers
        left, right = self._index_range(minValue, maxValue)
        if left < min(right, len(self.numbers)):
            del self.numbers[left:right]
        return max(0, right - left)

    def __iter__(self) -> Iterator[int]:
        #TODO code for ierating all numbers from NumberBox instance
        return iter(self.numbers)

    def distinct(self)->int:
        #Time complexity is O(n * log(n)). Space complexity is O(n).
        #TODO removing repeated numbers
        size: int = len(self.numbers)
        self.numbers = SortedList(dict.fromkeys(self.numbers))
        return size - len(self.numbers)