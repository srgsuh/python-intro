#https://leetcode.com/problems/regular-expression-matching/description/

class Solution(object):
    def isMatch(self, str: str, pattern: str) -> bool:
        rows: int = len(str)
        cols: int = len(pattern)
        joker: str = '*'
        
        memo = {}
        
        def dp(r: int, c: int) -> bool:
            if (r, c) in memo:
                return memo[(r, c)]
            
            result: bool = False
            if (c == cols):
                result = (r == rows)
            elif (r == rows):
                result = c + 1 < cols and pattern[c + 1] == joker and dp(r, c + 2)
            else:
                symbolMatch = pattern[c] == '.' or str[r] == pattern[c]
                if c + 1 < cols and pattern[c + 1] == joker:
                    result = dp(r, c + 2) or (symbolMatch and (
                        dp(r + 1, c) or dp(r + 1, c + 1)
                    ))
                else:
                    result = symbolMatch and dp(r + 1, c + 1)
            memo[(r, c)] = result
            
            return result            
            
        return dp(0, 0)