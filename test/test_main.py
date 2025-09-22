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
    def test_sum_of_two_inner(self):
        self.assertTrue(isSumTwo([1, 2, 1, 3, 0], 5))
        
    def test_sum_of_two_inner_negatives(self):
        self.assertTrue(isSumTwo([-1, -2, -1, -3, 0], -5))
    
    def test_no_sum_target_not_in_array(self):
        self.assertFalse(isSumTwo([1, 2, 3, 4], 9))
    
    def test_no_sum_target_in_array(self):
        self.assertFalse(isSumTwo([1, 2, 3, 4], 2))
        
    def test_no_sum_target_in_array_negative(self):
        self.assertFalse(isSumTwo([-1, -2, -3, -4], -2))
        
    def test_as_sum_of_two_last_entries(self):
        self.assertTrue(isSumTwo([1, 2, 3, 4], 7))
    
    def test_zero_as_sum_of_two_non_zeroes(self):
        self.assertTrue(isSumTwo([-1, 0, 5, 1], 0))
        
    def test_zero_as_sum_of_two_zeroes(self):
        self.assertTrue(isSumTwo([-1, 0, 5, 0], 0))
    
    def test_zero_with_one_zero_in_array(self):
        self.assertFalse(isSumTwo([-1, 0, 5, 2], 0))
        
    def test_two_elements_sum(self):
        self.assertTrue(isSumTwo([4, 5], 9))
        
    def test_two_identical_elements_sum(self):
        self.assertTrue(isSumTwo([-4, -4], -8))
    
    def test_two_elements_no_sum(self):
        self.assertFalse(isSumTwo([4, 5], 8))
    
    def test_one_element(self):
        self.assertFalse(isSumTwo([2], 2))
        
    def test_empty(self):
        self.assertFalse(isSumTwo([], 0))

class MaxNegativeReprTest(unittest.TestCase):
    def test_neg_one_element(self):
        self.assertEqual(maxNegativeRepr([100]), -1)
        
    def test_neg_empty(self):
        self.assertEqual(maxNegativeRepr([]), -1)
    
    def test_neg_all_zeroes(self):
        self.assertEqual(maxNegativeRepr([0, 0, 0, 0, 0]), -1)
    
    def test_neg_no_negative(self):
        self.assertEqual(maxNegativeRepr([1, 2, 100, 0, 8]), -1)
        
    def test_neg_no_positive(self):
        self.assertEqual(maxNegativeRepr([-1, -2, -100, 0, -8]), -1)
        
    def test_pos_zeroes_and_pair(self):
        self.assertEqual(maxNegativeRepr([0, -1, 0, 0, 0, 0, 1, 0]), 1)
    
    def test_pos_with_positive_after(self):
        self.assertEqual(maxNegativeRepr([-1, -2, -100, 0, 100, 1]), 100)
        
    def test_pos_with_negative_after(self):
        self.assertEqual(maxNegativeRepr([-1, -2, 100, 0, -100, 2]), 100)
    
    def test_pos_with_positive_after_as_last_entry(self):
        self.assertEqual(maxNegativeRepr([-1, -2, -100, 0, 100]), 100)
        
    def test_pos_with_negative_after_as_last_entry(self):
        self.assertEqual(maxNegativeRepr([-1, -2, 100, 0, -100]), 100)
        
    def test_pos_largest_pair_first(self):
        self.assertEqual(maxNegativeRepr([100, -100, 1, -1]), 100)
        
    def test_pos_with_several_options(self):
        self.assertEqual(maxNegativeRepr([-1, -2, 0, 100, 1, 2, 3, -3, -100]), 100)
    
    def test_pos_two_elements(self):
        self.assertEqual(maxNegativeRepr([-2, 2]), 2)

    def test_pos_repeat_the_same_pair(self):
        self.assertEqual(maxNegativeRepr([-2, 2, 2, -2, -2, 2, 2, -2]), 2)
    
        
if __name__ == '__main__':
    unittest.main()