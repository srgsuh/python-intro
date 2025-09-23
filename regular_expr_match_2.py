#https://leetcode.com/problems/regular-expression-matching/description/
from functools import lru_cache

class Solution(object):
    def isMatch(self, str: str, pattern: str) -> bool:
        rows: int = len(str)
        cols: int = len(pattern)
        joker: str = '*'
        
        def symbolMatch(s: str, p: str) -> bool:
            return p == '.' or p == s
                
        @lru_cache
        def dp(r: int, c: int) -> bool:
            if (c == cols):
                return r == rows
            if (r == rows):
                return c + 1 < cols and pattern[c + 1] == joker and dp(r, c + 2)
            if c + 1 < cols and pattern[c + 1] == joker:
                return dp(r, c + 2) or (symbolMatch(str[r], pattern[c]) and (
                    dp(r + 1, c) or dp(r + 1, c + 1)
                ))
            else:
                return symbolMatch(str[r], pattern[c]) and dp(r + 1, c + 1)
            return False
            
        return dp(0, 0)