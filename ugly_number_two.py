#https://leetcode.com/problems/ugly-number-ii/description/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if (n == 1):
            return 1
        numbers = [1]
        ugly = 1
        count = 1
        p2, p3, p5 = 0, 0, 0
        v2, v3, v5 = 2, 3, 5
        while True:
            ugly = min([v2, v3, v5])
            count += 1
            if count == n:
                break
            numbers.append(ugly)
            if (v2 == ugly):
                p2 += 1
                v2 = 2 * numbers[p2]
            if (v3 == ugly):
                p3 += 1
                v3 = 3 * numbers[p3]
            if (v5 == ugly):
                p5 += 1
                v5 = 5 * numbers[p5]
        return ugly