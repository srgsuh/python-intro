from array import array

class MyStackInt:
    def __init__(self):
        self._data = array('i')
        self._max = array('i')
    
    def push(self, val: int) -> None:
        """Add a new element to the top of the stack"""
        self._data.append(val)
        self._max.append(max(val, self.max() if self._max else val))
    
    def pop(self) -> int:
        """Remove the top element from the stack"""
        self._max.pop()
        return self._data.pop()
    
    def max(self) -> int:
        """Return the maximal element in the stack"""
        return self._max[-1]