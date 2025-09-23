import pytest
from regular_expr_match_2 import Solution

solution = Solution()

def test_match_10():
    assert True == solution.isMatch('a', 'ab*')

def test_match_10():
    assert True == solution.isMatch('aab', 'c*a*b')

def test_match_20():
    assert True == solution.isMatch('ab', '.*')

def test_match_30():
    assert False == solution.isMatch('aa', 'a')
    
def test_match_40():
    assert True == solution.isMatch('aa', 'a*')