#https://leetcode.com/problems/perfect-squares/description/
class Solution:
    def numSquares(self, n: int) -> int:
        squares: List[int] = []
        for i in range(n):
            j = (1 + i) * (1 + i)
            if j > n:
                break
            squares.append(j)
        if n == squares[-1]:
            return 1
        dp: List[int] = [0] * (1 + n)
        for p in range(1, n + 1):
            dp[p] = min(1 + dp[p - sqr] for sqr in squares if sqr <= p)
        return dp[n]