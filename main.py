from array import array

class MyStackInt:
    def __init__(self):
        self._data = array('i')
        self._max_idx = array('i')

    def _index_of_max(self):
        return self._max_idx[-1]

    def __len__(self):
        return len(self._data)
    
    def push(self, val: int) -> None:
        """Add a new element to the top of the stack"""
        self._data.append(val)
        if (not self._max_idx) or val > self.max():
            self._max_idx.append(len(self) - 1)
    
    def pop(self) -> int:
        """Remove the top element from the stack"""
        result = self._data.pop()
        if self._index_of_max() >= len(self):
            self._max_idx.pop()
        return result
    
    def max(self) -> int:
        """Return the maximal element in the stack"""
        return self._data[self._index_of_max()]