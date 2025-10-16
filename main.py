import math

class MyStackInt:
    def __init__(self):
        self._data = []
    
    def push(self, val: int) -> None:
        """Add new element to the top of the stack"""
        self._data.append((val, max(self.max() if self._data else val, val)))
    
    def pop(self) -> int:
        """Remove the top element from the stack"""
        return self._data.pop()[0]
    
    def max(self) -> int:
        """Return the maximal element in the stack"""
        return self._data[-1][1]