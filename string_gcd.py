#https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def is_divisor(s1: str, s2: str) -> bool:
            print(f" s1 = {s1}, s2 = {s2}, div = {s2 * (len(s2) // len(s1))}")
            return s2 * (len(s1) // len(s2)) == s1

        int_gcd = math.gcd(len(str1), len(str2))
        str_gcd = str1[:int_gcd]

        if is_divisor(str2, str_gcd) and is_divisor(str1, str_gcd):
            return str_gcd

        return ""

s: Solution = Solution()
print(f"gcd('ABCABC', 'ABC') == \"{s.gcdOfStrings("ABCABC", "ABC")}\"")