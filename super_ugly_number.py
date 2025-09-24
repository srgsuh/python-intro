#https://leetcode.com/problems/super-ugly-number/description/

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if (n == 1):
            return 1
        k: int = len(primes)
        pointers = [0] * k
        values = primes[:]
        numbers = [1]
        ugly = 1
        count = 1
        while True:
            ugly = min(values)
            count += 1
            if count == n:
                break
            numbers.append(ugly)
            for idx, v in enumerate(values):
                if v == ugly:
                    pointers[idx] += 1
                    values[idx] = primes[idx] * numbers[ pointers[idx] ]
        
        return ugly