class Solution(object):
    def isMatch(self, str, pattern):
        self.str = str
        self.pattern = pattern
        self.dp = [[-1 for _ in range(1 + len(pattern))] for __ in range(1 + len(str))]
        return 1 == self.__matcher(0, 0)
        
    def __matcher(self, s_idx, p_idx):
        if (self.dp[s_idx][p_idx] != -1):
            return self.dp[s_idx][p_idx]
        if s_idx == len(self.str):
            if p_idx == len(self.pattern) or (self.pattern[p_idx] == '*' and self.__matcher(s_idx, 1 + p_idx)):
                self.dp[s_idx][p_idx] = 1
            else:
                self.dp[s_idx][p_idx] = 0
        else:
            if p_idx == len(self.pattern):
                self.dp[s_idx][p_idx] = 0
            elif self.pattern[p_idx] == '?':
                self.dp[s_idx][p_idx] = self.__matcher(s_idx + 1, p_idx + 1)
            elif self.pattern[p_idx] != '*':
                self.dp[s_idx][p_idx] = self.str[s_idx] == self.pattern[p_idx] and self.__matcher(s_idx + 1, p_idx + 1)
            else:
                if self.__matcher(s_idx + 1, p_idx) or self.__matcher(s_idx, p_idx + 1):
                    self.dp[s_idx][p_idx] = 1
                else:
                    self.dp[s_idx][p_idx] = 0
        
        return self.dp[s_idx][p_idx]

solution = Solution()
print(solution.isMatch("aa", "a."))