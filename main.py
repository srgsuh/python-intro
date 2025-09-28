import sortedcontainers as sc
from sortedcontainers import SortedList

numbers: sc.SortedList = sc.SortedList()
numbers.add(30)
numbers.add(20)
numbers.add(50)
numbers.add(3)
numbers.add(10)

def get_numbers_range(arr: SortedList, min_val: int, max_val: int) -> list[int]:
    """Returns a list of numbers from the given array that are within the given range inclusively."""
    left: int = arr.bisect_left(min_val)
    right: int = arr.bisect_right(max_val)
    return arr[left:right]

if __name__ == '__main__':
    print(numbers)
    print(get_numbers_range(numbers, 20, 30))