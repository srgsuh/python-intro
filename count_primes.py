#https://leetcode.com/problems/count-primes/description/
class Solution:
    def countPrimes(self, n: int) -> int:
        primes =  [False, False] + [True] * (n - 2)
        primeCount = 0
        for p in range(n):
            if primes[p]:
                primeCount += 1
                for i in range(p + p, n, p):
                    primes[i] = False
        return primeCount