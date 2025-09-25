import pytest
from fraction_to_decimal import Solution

solution: Solution = Solution()

def test_1_over_2():
    assert "0.5" == solution.fractionToDecimal(1, 2)
    
def test_1_over_8():
    assert "0.125" == solution.fractionToDecimal(1, 8)
    
def test_2_over_1():
    assert "2" == solution.fractionToDecimal(2, 1)
    
def test_1_over_3():
    assert "0.(3)" == solution.fractionToDecimal(1, 3)

def test_4_over_333():
    assert "0.(012)" == solution.fractionToDecimal(4, 333)

def test_1_over_14():
    assert "0.0(714285)" == solution.fractionToDecimal(1, 14)
    
def test_minus50_over_8():
    assert "-6.25" == solution.fractionToDecimal(-50, 8)