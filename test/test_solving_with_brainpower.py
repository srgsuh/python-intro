import pytest
from solving_with_brainpower import Solution

solution: Solution = Solution()

def test_01():
    assert 5 == solution.mostPoints([[3,2],[4,3],[4,4],[2,5]])