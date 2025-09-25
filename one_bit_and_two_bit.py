#https://leetcode.com/problems/1-bit-and-2-bit-characters/description/
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:    
        i, n = 0, len(bits)
        while i < n - 1:
            i += 2 if bits[i] == 1 else 1
        return i == n - 1 