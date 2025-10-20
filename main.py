class MyArray[T]:
    def __init__(self, size: int):
        """Create a new array instance with capacity of `size`."""
        pass

    def get(self, index: int) -> T:
        """Return the element at index `index`."""
        raise NotImplementedError()

    def set(self, index: int, value: T):
        """Set the element at index `index` to `value`."""
        raise NotImplementedError()

    def setAll(self, value: T):
        """Set all elements to `value`."""
        raise NotImplementedError()
