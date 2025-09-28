import bisect

numbers: list[int] = []
bisect.insort(numbers, 30)
bisect.insort(numbers, 20)
bisect.insort(numbers, 50)
bisect.insort(numbers, 3)
bisect.insort(numbers, 10)

def get_numbers_range(arr: list[int], min_val: int, max_val: int) -> list[int]:
    """Returns a list of numbers from the given array that are within the given range inclusively."""
    left: int = bisect.bisect_left(arr, min_val)
    right: int = bisect.bisect_right(arr, max_val)
    return arr[left:right]

if __name__ == '__main__':
    print(numbers)
    print(get_numbers_range(numbers, 0, 1))