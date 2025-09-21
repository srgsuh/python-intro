import pytest
from regular_expr_match import Solution

solution = Solution()

def test_isMatch_01():
    assert False == solution.isMatch("aa", "a")

def test_isMatch_02():
    assert True == solution.isMatch("aa", "a*")

def test_isMatch_03():
    assert True == solution.isMatch("aa", "*")

def test_isMatch_04():
    assert True == solution.isMatch("ab", "?*")

def test_isMatch_05():
    assert True == solution.isMatch("abcd", "?*")