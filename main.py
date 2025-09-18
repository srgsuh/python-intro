def bSearchSortedList(lst: list[int], target: int) -> int:
    # Binary search in a sorted list, returns the index of the target or -1 if not found
    left: int = 0
    right: int = len(lst) - 1

    while left <= right:
        mid: int = left + (right - left) // 2
        if (lst[mid] == target):
            return mid
        elif (lst[mid] > target):
            right = mid - 1
        else:
            left = mid + 1
    
    return -1


nums: list[int] = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(bSearchSortedList(nums, 70))
print(bSearchSortedList(nums, 25))