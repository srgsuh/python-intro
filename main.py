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
    left: int = -1
    right: int = len(sorted_list)

    while (right - left) > 1:
        mid: int = left + (right - left) // 2
        if (sorted_list[mid] >= target):
            right = mid
        else:
            left = mid

    return right if (right < len(sorted_list) and sorted_list[right] == target) else -(right + 1)