import pytest
from subarrays_with_k_values import Solution

s: Solution = Solution()

def test_01():
    assert 12 == s.atMostK([1, 2, 1, 2, 3], 2)
    assert 5 == s.atMostK([1, 2, 1, 2, 3], 1)