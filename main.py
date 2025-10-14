from collections import OrderedDict
from dataclasses import dataclass, field
from typing import Generic, Hashable, TypeVar

from sortedcontainers import SortedSet
K = TypeVar('K', bound=Hashable)
V = TypeVar("V")
@dataclass(order=True, frozen=True)
class Entry(Generic[K, V]):
    key: K
    value: V = field(compare=False, hash=False)
    def __str__(self):
        return f"'{self.key}': {self.value}"
    
class MyDict(Generic[K, V]):
    def __init__(self):
        self.__entries: set[Entry[K, V]] = set()
    def __getitem__(self, key: K) -> V :
        entry: Entry[K, V] = self.__getEntryByKey(key)
        if not entry:
            raise KeyError(key)
        return entry.value
    def __setitem__(self, key: K, value: V):
        probe: Entry[K, V] = Entry(key, value)
        self.__entries.discard(probe)
        self.__entries.add(probe)
    def __getEntryByKey(self, key: K) -> Entry[K, V]:
        # our implementation is O[N], but built-in implementation is O[1] 
        res: Entry[K, V] = None
        probe: Entry[K, V] = Entry(key, None)
        if probe in self.__entries:
            res = next((e for e in self.__entries if e == probe))
        return res
    def __str__(self) :
        return  '{' + ", ".join([str(e) for e in self.__entries]) + '}'
    
    # HW #24
    def __len__(self):
        # returns count of the entries
        # this is a magic method allowing using the function len of Python
        return len(self.__entries)

    def setdefault(self, key: K, default: V = None):
        # If key missing, insert key: default; return the default.
        # If key exists, no insert, no update; return the value
        entry: Entry[K, V] = self.__getEntryByKey(key)
        if not entry:
            self.__setitem__(key, default)
        return entry.value if entry else default
    
    def get(self, key: K, default: V = None):
        # returns value for key or any default if key missing
        entry: Entry[K, V] = self.__getEntryByKey(key)
        return entry.value if entry else default
    
    def items(self) -> list[tuple[K, V]]:
        # returns list of tuples (key, value)
        # tuple is an immutable list 
        # [1, 2] - list, (1, 2) - tuple
        # assume that e is Entry, then to create tuple from Entry e - (e.key, e.value)
        # try to write one code line using so called comprehension expresson
        # [<expression with item> for <item> in <items>] 
       return [(e.key, e.value) for e in self.__entries]
    
    def keys(self) -> list[K]:
        # returns list of keys
        return [e.key for e in self.__entries]
    
    def values(self) -> list[V]:
        # returns list of values
        return [e.value for e in self.__entries]
    
    def update(self, key: K, value: V):
        # if key exists, updates value for the key
        # if key missing, inserts key: value entry
        self[key] = value

    _sentinel = object()
    def pop(self, key: K, default=_sentinel)->V:
        # removes key if the key exists, return the associated value
        # line 72 with default value is intended for differentiating optional parameter. As None may be value passed by a caller 
        # if default is _sentinel, a caller has not passed default value.
        # Operator "is" implies the same reference. It differs from '==' (equility) 
        # if key missing and default value having been passed that value will be returned
        # if key missing and default value not passed KeyError should be raised
        entry: Entry[K, V] = self.__getEntryByKey(key)
        if entry:
            self.__entries.discard(entry)
            result = entry.value
        else:
            result = default

        if result is self._sentinel:
            raise KeyError(key)

        return result
        
 ###########################################################################################
class MySortedDict[K,V]:
    def __init__(self) :
        self.__entries: SortedSet[K, V] = SortedSet()

    def __get_by_key(self, key: K) -> Entry[K, V]:
        index: int = self.bisect_left(key)
        entry = self.__entries[index] if index < len(self) else None
        return entry if entry and entry.key == key else None
    
    def __getitem__(self, key: K) -> V :
        # see implementation of MyDict,
        # but it should be implemented with O[LogN] complexity
        entry: Entry[K, V] = self.__get_by_key(key)
        if not entry:
            raise KeyError(key)
        return entry.value

    def __setitem__(self, key: K, value: V):
        # see implementation of MyDict, O[LogN] complexity
        entry: Entry[K, V] = Entry(key, value)
        self.__entries.discard(entry)
        self.__entries.add(entry)
    
    def __str__(self) :
        return  '{' + ", ".join([str(e) for e in self.__entries]) + '}'
    
    def __len__(self):
        # returns count of the entries
        # this is a magic method allowing using the function len of Python
        return len(self.__entries)

    def setdefault(self, key: K, default: V = None):
        # If key missing, insert key: default; return the default.
        #    If key exists, no insert, no update; return the value
        entry: Entry[K, V] = self.__get_by_key(key)
        if not entry:
            self.__setitem__(key, default)
        return entry.value if entry else default
    
    def get(self, key: K, default: V = None):
        # returns value for key or any default if key missing
        # O[LogN] complexity
        entry: Entry[K, V] = self.__get_by_key(key)
        return entry.value if entry else default
    
    def items(self) -> list[(K,  V)]:
        # returns list of tuples (key, value)
        # tuple is an immutable list 
        # [1, 2] - list, (1, 2) - tuple
        # assume that e is Entry, then to create tuple from Entry e - (e.key, e.value)
        # try to write one code line using so called comprehension expresson
        # [<expression with item> for <item> in <items>] 
       return [(e.key, e.value) for e in self.__entries]
    
    def keys(self) -> list[K]:
        # returns list of keys
        return [e.key for e in self.__entries]
    
    def values(self) -> list[V]:
        # returns list of values
        return [e.value for e in self.__entries]
    
    def update(self, key: K, value: V):
        # if key exists, updates value for the key
        # if key missing, inserts key: value entry
        self[key] = value

    _sentinel = object()
    def pop(self, key: K, default=_sentinel) -> V:
        # removes key if the key exists with returning associated value
        # if key missing and default exists, returns default
        entry: Entry[K, V] = self.__get_by_key(key)
        if entry:
            self.__entries.discard(entry)
        result = entry.value if entry else default
        if result is self._sentinel:
            raise KeyError(key)
        return result

    def bisect_left(self, key:K)->int:
        # returns first index of key that >= a given key
        return self.__entries.bisect_left(Entry(key, None))

    def bisect_right(self, key:K)->int:
        # returns first index of key that > a given key
        return self.__entries.bisect_right(Entry(key, None))

    def peekitem(self, ind: int)->tuple[K,V] :
        # returns received from Entry tuple at a specified index
        # may take a negative index with meaning the indexing from the end (index -1 designates the kast key
        # raises error for an index out of a possible range (index < -len(self) or index >= len(self))
        entry = self.__entries[ind]
        return entry.key, entry.value
  ####################################################################################
  
class DictCache(OrderedDict[K, V]) :
    def __init__(self, maxsize=128):
        super().__init__() # calls constructor of OrderedDict that has all methods for keeping insertion order
        self.maxsize = maxsize
    #
    # The  methods __getitem__ and __setitem__ should be overriden
    # Assumption: only following methods should be overriden for making tests from test_dict_cache.py passed
    # Hints as follows: 
    # super().__getitem__(key) calls method __getitem__ of OrderedDict
    # super().__setitem__(key, value) calls method __setitem__ of OrderedDict
    # consider using self.move_to_end(key) of OrderedDict for making item with the given key as most recent
    # consider using self.popitem(last=False) for removing least recent (eldest item)
    
    def __getitem__(self, key):
        self.move_to_end(key)
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        if key in self:
            self.move_to_end(key)
        elif len(self) == self.maxsize:
            self.popitem(last=False)
        super().__setitem__(key, value)