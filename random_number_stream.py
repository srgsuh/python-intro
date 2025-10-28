import itertools as it
from typing import Callable, Iterator
from random import Random

def unique_filter(iterator: Iterator[int]) -> Iterator[int]:
    yielded_values: set[int] = set()
    for x in iterator:
        if x not in yielded_values:
            yielded_values.add(x)
            yield x

class RandomNumbersStream:
    _gen: Random = Random()
    def __init__(self, min: int = -10 ** 20, max: int = 10 ** 20):
        if max < min:
            min, max = max, min
        self._max: int = max
        self._min: int = min
        self._limit: int = 0
        self._predicate: Callable[[int], bool] | None = None
        self._is_unique: bool = False
    
    def setFilter(self, predicate: Callable[[int], bool]):
        self._predicate = predicate
    
    def setLimit(self, limit: int):
        """Limit maximum amount of values the stream might produce. The limit of 0 means unlimited"""
        if limit < 1:
            raise ValueError("Limit must be non-negative")
        self._limit = limit
    
    def setDistinct(self):
        self._is_unique = True
    
    def resetDistinct(self):
        self._is_unique = False
    
    def __iter__(self) -> Iterator[int]:
        iter: Iterator[int] = (self._gen.randint(l, r) for l, r in it.repeat((self._min, self._max)))
        iter = iter if self._predicate is None else (x for x in iter if self._predicate(x))
        iter = iter if not self._is_unique else unique_filter(iter)
        iter = iter if not self._limit else it.islice(iter, self._limit)
        
        return iter
        
    
if __name__ == "__main__":
    stream = RandomNumbersStream(10, 100)
    stream.setLimit(10)
    it1 = iter(stream)
    stream.setFilter(lambda x: x % 2 == 0)
    stream.setDistinct()
    it2 = iter(stream)

    print([x for x in it1])
    print([x for x in it2])
