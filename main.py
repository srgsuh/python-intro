from itertools import count, islice
from typing import Iterator, Iterable


class NumbersStream:
    def __init__(self, start: int = 0):
        self.start = start

    def __iter__(self) -> Iterator[int]:
        return count(self.start)
    
    def limit(self, limit_value: int) -> Iterable[int]:
        return islice(self, limit_value)


def print_it(it: Iterable):
    for i in it:
        print(i)


if __name__ == "__main__":
    stream: NumbersStream = NumbersStream(1).limit(20)
    filtered_gen = (v for v in stream if v % 2)
    list = [x for x in stream if x % 2]
    print_it(list)
    print_it(filtered_gen)
    print_it([x for x in stream if x % 2])