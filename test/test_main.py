import pytest
from main import bSearchSortedList

nums: list[int] = [10, 10, 10, 20, 30, 30, 40, 50, 60, 70, 80, 90, 90, 90, 90]

def test_bSearchSortedList_found_10():
    assert bSearchSortedList(nums, 10) == 0

def test_bSearchSortedList_found_20():
    assert bSearchSortedList(nums, 20) == 3

def test_bSearchSortedList_found_30():
    assert bSearchSortedList(nums, 30) == 4
    
def test_bSearchSortedList_found_90():
    assert bSearchSortedList(nums, 90) == 11

def test_bSearchSortedList_not_found_1():
    assert bSearchSortedList(nums, 1) == -1
    
def test_bSearchSortedList_not_found_43():
    assert bSearchSortedList(nums, 43) == -8

def test_bSearchSortedList_not_found_99():
    assert bSearchSortedList(nums, 99) == -16
    
def test_bSearchSortedList_ten_zeroes_0():
    assert bSearchSortedList([0,0,0,0,0,0,0,0,0,0], 0) == 0
    
def test_bSearchSortedList_ten_zeroes_one():
    assert bSearchSortedList([0,0,0,0,0,0,0,0,0,0], 1) == -11

def test_bSearchSortedList_ten_zeroes_minus_one():
    assert bSearchSortedList([0,0,0,0,0,0,0,0,0,0], -1) == -1
    
def test_bSearchSortedList_012_one():
    assert bSearchSortedList([0,1,2], 1) == 1

def test_bSearchSortedList_012_two():
    assert bSearchSortedList([0,1,2], 2) == 2