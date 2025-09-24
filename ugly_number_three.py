class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm(x: int, y: int) -> int:
            return (x // math.gcd(x, y)) * y
        
        ab: int = lcm(a, b)
        bc: int = lcm(b, c)
        ac: int = lcm(a, c)
        abc: int = lcm(ab, c)
        
        def countUgly(L: int) -> int:
            return L//a + L//b + L//c - L//ab - L//bc - L//ac + L//abc
        
        maxV: int = 1 + n * min(a, b, c)
        l, r = 0, maxV
        while (l < r):
            m: int = l + (r - l) // 2
            cnt: int = countUgly(m)
            if cnt < n:
                l = m + 1
            else:
                r = m
        return l