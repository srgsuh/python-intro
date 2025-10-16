from array import array

class MyStackInt:
    def __init__(self):
        self._data = array('i')
        self._max = array('i')
    
    def push(self, val: int) -> None:
        """Add a new element to the top of the stack"""
        self._data.append(val)
        if not self._max or val >= self.max():
            self._max.append(val)
    
    def pop(self) -> int:
        """Remove the top element from the stack"""
        val = self._data.pop()
        if val == self.max():
            self._max.pop()
        return val
    
    def max(self) -> int:
        """Return the maximal element in the stack"""
        return self._max[-1]