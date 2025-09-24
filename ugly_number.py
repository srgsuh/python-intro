class Solution:
    def isUgly(self, n: int) -> bool:
        for f in [2, 3, 5]:
            while n % f == 0:
                n /= f
        return n == 1