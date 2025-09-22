def bSearchSortedList(sorted_list: list[int], target: int) -> int:
    """
    Perform a binary search on a sorted list with duplicates allowed.
    Returns the index of the first occurrence of the target if found,
    otherwise returns -(insert_index + 1), where insert_index is the index
    at which the target can be inserted to keep the list sorted.
    """
    n: int = len(sorted_list)
    left: int = 0
    right: int = n

    while left < right:
        mid: int = left + (right - left) // 2
        if (sorted_list[mid] < target):
            left = mid + 1
        else:
            right = mid

    return left if (left < n and sorted_list[left] == target) else -(left + 1)

def isSumTwo(nums: list[int], target: int) -> bool:
    return False

def maxNegativeRepr(nums: list[int]) -> int:
    maxValue: int = -1
    passed = set()
    
    for v in nums:
        if v != 0:
            if -v in passed:
                maxValue = max(maxValue, abs(v))
            passed.add(v)
    
    return maxValue
            

if __name__ == '__main__':
    nums: list[int] = [-1, -1, 0, 2, 3]
    print(bSearchSortedList(nums, -1))
    print(bSearchSortedList(nums, 1))
