def bSearchSortedList(sorted_list: list[int], target: int) -> int:
    """
    Perform a binary search on a sorted list with duplicates allowed.
    Returns the index of the first occurrence of the target if found,
    otherwise returns -(insert_index + 1), where insert_index is the index
    at which the target can be inserted to keep the list sorted.
    
    Args:
        sorted_list (list[int]): The sorted list to search.
        target (int): The target value to find.

    Returns:
        int: the index of the first occurrence of the target if found, otherwise -(insert_index + 1).
    """
    left: int = 0
    right: int = len(sorted_list) - 1

    while left <= right:
        mid: int = left + (right - left) // 2
        if (sorted_list[mid] >= target):
            right = mid - 1
        else:
            left = mid + 1

    return left if (left < len(sorted_list) and sorted_list[left] == target) else -(left + 1)