class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1 if i < 2 else 0 for i in range(n + 1)]        
        
        def count(p: int):
            if (dp[p] == 0):
                for i in range(0, p):
                    dp[p] += count(i) * count(p - i - 1)
            
            return dp[p]
        
        return count(n)