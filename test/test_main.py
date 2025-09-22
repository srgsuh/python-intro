from main import bSearchSortedList, isSumTwo, maxNegativeRepr
import unittest

class BinarySearchTest(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.nums: list[int] = [10, 10, 10, 20, 30, 30, 40, 50, 60, 70, 80, 90, 90, 90, 90]
    
    def test_found_10(self):
        self.assertEqual(bSearchSortedList(self.nums, 10), 0)
        
    def test_found_20(self):
        self.assertEqual(bSearchSortedList(self.nums, 20), 3)
        
    def test_found_30(self):
        self.assertEqual(bSearchSortedList(self.nums, 30), 4)
    
    def test_found_90(self):
        self.assertEqual(bSearchSortedList(self.nums, 90), 11)
    
    def test_not_found_43(self):
        self.assertEqual(bSearchSortedList(self.nums, 43), -8)
        
    def test_not_found_99(self):
        self.assertEqual(bSearchSortedList(self.nums, 99), -16)
        
    def test_not_found_1(self):
        self.assertEqual(bSearchSortedList(self.nums, 1), -1)
    
    def test_empty_list(self):
        self.assertEqual(bSearchSortedList([], 1), -1)

class IsSumTwoTest(unittest.TestCase):
    def test_isSumTwo_sum_of_two_inner(self):
        self.assertTrue(isSumTwo([1, 2, 1, 3, 0], 5))
        
    def test_isSumTwo_sum_of_two_inner_negatives(self):
        self.assertTrue(isSumTwo([-1, -2, -1, -3, 0], -5))
    
    def test_isSumTwo_no_sum_target_not_in_array(self):
        self.assertFalse(isSumTwo([1, 2, 3, 4], 9))
    
    def test_isSumTwo_no_sum_target_in_array(self):
        self.assertFalse(isSumTwo([1, 2, 3, 4], 2))
        
    def test_isSumTwo_no_sum_target_in_array_negative(self):
        self.assertFalse(isSumTwo([-1, -2, -3, -4], -2))
        
    def test_isSumTwo_as_sum_of_two_last_entries(self):
        self.assertTrue(isSumTwo([1, 2, 3, 4], 7))
    
    def test_isSumTwo_zero_as_sum_of_two_non_zeroes(self):
        self.assertTrue(isSumTwo([-1, 0, 5, 1], 0))
        
    def test_isSumTwo_zero_as_sum_of_two_zeroes(self):
        self.assertTrue(isSumTwo([-1, 0, 5, 0], 0))
    
    def test_isSumTwo_zero_with_one_zero_in_array(self):
        self.assertFalse(isSumTwo([-1, 0, 5, 2], 0))
    
    def test_isSumTwo_one_element(self):
        self.assertFalse(isSumTwo([2], 2))
        
    def test_isSumTwo_empty(self):
        self.assertFalse(isSumTwo([], 0))
        
if __name__ == '__main__':
    unittest.main()