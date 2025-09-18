import pytest
from main import bSearchSortedList

nums: list[int] = [10, 20, 30, 40, 50, 60, 70, 80, 90]

def test_bSearchSortedList_found_10():
    assert bSearchSortedList(nums, 10) == 0

def test_bSearchSortedList_found_30():
    assert bSearchSortedList(nums, 30) == 2
    
def test_bSearchSortedList_found_90():
    assert bSearchSortedList(nums, 90) == 8

def test_bSearchSortedList_not_found_1():
    assert bSearchSortedList(nums, 1) == -1
    
def test_bSearchSortedList_not_found_43():
    assert bSearchSortedList(nums, 43) == -5

def test_bSearchSortedList_not_found_99():
    assert bSearchSortedList(nums, 99) == -10