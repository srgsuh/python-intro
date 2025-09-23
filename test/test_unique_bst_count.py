import pytest
from unique_bst_count import Solution

solution: Solution = Solution()

def test_1():
    assert 1 == solution.numTrees(1)

def test_2():
    assert 2 == solution.numTrees(2)

def test_3():
    assert 5 == solution.numTrees(3)

def test_4():
    assert 14 == solution.numTrees(4)

def test_5():
    assert 42 == solution.numTrees(5)
    
def test_6():
    assert 132 == solution.numTrees(6)

def test_7():
    assert 429 == solution.numTrees(7)

def test_8():
    assert 1430 == solution.numTrees(8)