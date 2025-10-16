import math

class MyStackInt:
    def __init__(self):
        self._data = []
        self._max_values = [-math.inf]
    
    def push(self, val: int) -> None:
        """Add new element to the top of the stack"""
        self._data.append(val)
        if val >= self._max_values[-1]:
            self._max_values.append(val)
    
    def pop(self) -> int:
        """Remove the top element from the stack"""
        result = self._data.pop()
        if result >= self._max_values[-1]:
            self._max_values.pop()
        
        return result
    
    def max(self) -> int:
        """Return the maximal element in the stack"""
        if len(self._max_values) < 2:
            raise IndexError()
        return self._max_values[-1]
    
st = MyStackInt()
st.push(1)
st.push(2)
print(st.max())
st.pop()
print(st.max())