import itertools as it
from typing import Callable, Iterator
from random import Random

def unique_filter(iterator: Iterator[int]) -> Iterator[int]:
    yielded_values: set[int] = set()
    for x in iterator:
        if x not in yielded_values:
            yielded_values.add(x)
            yield x

class RandomStreamBuilder:
    _gen: Random = Random()

    def __init__(self, min: int, max: int):
        self.stream: Iterator[int] = (self._gen.randint(l, r) for l, r in it.repeat((min, max)))
    
    def filter(self, callable: Callable[[int], bool] | None = None) -> "RandomStreamBuilder":
        self.stream = self.stream if callable is None else (v for v in self.stream if callable(v))
        return self

    def limit(self, max_values: int = 0) -> "RandomStreamBuilder":
        self.stream = self.stream if not max_values else it.islice(self.stream, max_values)
        return self
    
    def unique(self, is_unique: bool = True) -> "RandomStreamBuilder":
        self.stream = unique_filter(self.stream) if is_unique else self.stream
        return self

    def build(self) -> Iterator[int]:
        return self.stream

class RandomNumbersStream:
    def __init__(self, min: int = -10 ** 20, max: int = 10 ** 20):
        if max < min:
            raise ValueError("max cannot be less then min")
        self._max: int = max
        self._min: int = min
        self._limit: int = 0
        self._filter: Callable[[int], bool] | None = None
        self._is_unique: bool = False
    
    def setFilter(self, predicate: Callable[[int], bool]):
        self._filter = predicate
    
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
        builder = RandomStreamBuilder(self._min, self._max)
        return builder.filter(self._filter).unique(self._is_unique).limit(self._limit).build()
        
    
if __name__ == "__main__":
    stream = RandomNumbersStream(10, 100)
    stream.setLimit(25)
    it1 = iter(stream)
    stream.setFilter(lambda x: x % 2 == 0)
    stream.setDistinct()
    it2 = iter(stream)

    print([x for x in it1])
    print([x for x in it2])
