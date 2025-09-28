#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        usedChars = set()
        n, start, end = len(s), 0, 0
        while end < n:
            if s[end] not in usedChars:
                usedChars.add(s[end])
                end += 1
                maxLength = max(maxLength, end - start)
            else:
                usedChars.remove(s[start])
                start += 1
        return maxLength