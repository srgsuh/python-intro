from dataclasses import dataclass

@dataclass(frozen=True)
class Entry[T]:
    value: T
    updated_on: int

class MyArray[T]:
    def __init__(self, size: int):
        """Create a new MyArray instance with the provided capacity."""
        self._size: int = size
        self._tick: int = 0
        self._entries: dict[int, Entry[T]] = {}
        self._global: T | None = None

    def _index_check(self, index: int):
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of range")

    def get(self, index: int) -> T:
        """Return the element at index."""
        self._index_check(index)
        result = self._global if self._global else None
        personal: Entry[T] = self._entries.get(index, None)
        if personal and personal.updated_on >= self._tick:
            result = personal.value
        if result is None:
            raise ValueError(f"Value at index {index} is not defined")

        return result

    def set(self, index: int, value: T):
        """Set the element value at index."""
        self._index_check(index)
        self._entries[index] = Entry(value, self._tick)

    def setAll(self, value: T):
        """Set value to all elements in the array."""
        self._tick += 1
        self._global = value

