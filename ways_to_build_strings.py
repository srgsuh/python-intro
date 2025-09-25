#https://leetcode.com/problems/count-ways-to-build-good-strings/description/

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        modulo = 1_000_000_007
        
        ways = [0] * (high + 1)
        ways[0] = 1
        
        for p in range(high):
            if p + zero <= high:
                ways[p + zero] = add(ways[p + zero], ways[p])
            if p + one <= high:
                ways[p + one] = add(ways[p + one], ways[p])
        
        total = 0
        for i in range(low, high + 1):
            total = add(total, ways[i])
        
        return sum