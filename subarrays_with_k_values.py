# https://leetcode.com/problems/subarrays-with-k-different-integers/description/
# Given an integer array nums and an integer k, return the number of good subarrays of nums.
# A good array is an array where the number of different integers in that array is exactly k.
#     For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.

class Solution:
    def atMostK(self, a: list[int], k: int):
        if k == 0:
            return 0
        passed = {}
        n, left, right, count = len(a), 0, 0, 0
        while left < n:
            if right < n and (len(passed) < k or (len(passed) == k and a[right] in passed)):
                passed[a[right]] = passed.get(a[right], 0) + 1
                right += 1
                count += (right - left)
            else:
                if right == n:
                    break
                else:
                    while left < right and len(passed) >= k:
                        ch = a[left]
                        if passed[ch] > 1:
                            passed[ch] -= 1
                        else:
                            passed.pop(ch)
                        left += 1
        return count
                
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)