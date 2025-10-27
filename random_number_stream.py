import itertools as it
from typing import Callable, Iterator, Iterable

class RandomNumbersStream:
    def __init__(self,min: int = -10 ** 20, max: int = 10 ** 20):
        raise NotImplementedError()
    
    def setFilter(self, predicate: Callable[[int], bool]):
        raise NotImplementedError()
    
    def setLimit(self, limit: int):
        raise NotImplementedError()
    
    def setDistinct(self):
        raise NotImplementedError()
    
    def resetDistinct(self):
        raise NotImplementedError()
    
    def __iter__(self) -> Iterator[int]:
        raise NotImplementedError()