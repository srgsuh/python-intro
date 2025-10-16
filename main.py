import math

class MyStackInt:
    def __init__(self):
        self._data = []
        self._max_values = []
    
    def push(self, val: int) -> None:
        """Add new element to the top of the stack"""
        self._data.append(val)
        if val >= (self._max_values[-1] if self.max_values else val):
            self._max_values.append(val)
    
    def pop(self) -> int:
        """Remove the top element from the stack"""
        result = self._data.pop()
        if result >= self._max_values[-1]:
            self._max_values.pop()
        
        return result
    
    def max(self) -> int:
        """Return the maximal element in the stack"""
        return self._max_values[-1]
    
st = MyStackInt()
print(st.pop())