class MyArray[T]:
    def __init__(self, size: int):
        """Create a new MyArray instance with the provided capacity."""
        self._size: int = size
        self._data: dict[int, int] = {}
        self._global: T | None = None

    def _index_check(self, index: int) -> None:
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of range")

    def get(self, index: int) -> T:
        """Return the element at index."""
        self._index_check(index)
        local = self._data.get(index, None)
        result = local if local is not None else self._global
        if result is None:
            raise ValueError(f"Value at index {index} is not defined")

        return result

    def set(self, index: int, value: T) -> None:
        """Set the element value at index."""
        self._index_check(index)
        self._data[index] = value

    def setAll(self, value: T) -> None:
        """Set value to all elements in the array."""
        self._global = value
        self._data = {}

