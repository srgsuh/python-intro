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