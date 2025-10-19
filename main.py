from typing import Callable, Iterator, Iterable
from sortedcontainers import SortedList

_last_visited = object()

class NumberBox():
    #constructor defining most effective data structure
    def __init__(self, iterable: Iterable[int] = None):
        #Time complexity is O(n*log(n)), where n is the number of elements in the iterable.
        self.numbers = SortedList(iterable)

    def addNumber(self, num: int):
        #adds number
        #Time complexity is O(log n)
        self.numbers.add(num)

    def removeNumber(self,num: int)->int:
        #removes first occurrence of number and returns removed number or None if number missing
        #Time complexity is O(log(n))
        value: int | None = None
        index = self.numbers.bisect_left(num)
        if index < len(self.numbers) and self.numbers[index] == num:
            del self.numbers[index]
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
        #removes all numbers matching a given predicate
        #predicate - function taking integer and returning True if the integer matches the predicate otherwise False
        #returns count of the removed numbers

        #Time complexity is O(n*log(n)). Space complexity is O(n).
        checked_cache: dict[int, bool] = dict()
        def _pred_cache(x: int) -> bool:
            if x not in checked_cache:
                checked_cache[x] = pred(x)
            return checked_cache[x]

        initial_size: int = len(self.numbers)
        self.numbers = SortedList(x for x in self.numbers if not _pred_cache(x))
        return initial_size - len(self.numbers)

    def removeNumbersRange(self, minValue: int, maxValue: int)->int:
        #removes all numbers that >=min and <=max
        #returns count of removed numbers
        #Time complexity is O(log n)
        left, right = self._index_range(minValue, maxValue)
        if left < min(right, len(self.numbers)):
            del self.numbers[left:right]
        return max(0, right - left)

    def __iter__(self) -> Iterator[int]:
        #code for ierating all numbers from NumberBox instance
        return iter(self.numbers)

    def distinct(self)->int:
        #Time complexity is O(n * log(n)). Space complexity is O(n).
        #removing repeated numbers
        size: int = len(self.numbers)
        self.numbers = SortedList(dict.fromkeys(self.numbers))
        return size - len(self.numbers)
