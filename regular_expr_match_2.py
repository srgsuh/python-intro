#https://leetcode.com/problems/regular-expression-matching/description/

class Solution(object):
    def cmp(self, r, c):
        if self.dp[r][c] == -1:
            isJoker = c < self.cols - 1 and self.pattern[c + 1] == '*'
            if c == self.cols:
                self.dp[r][c] = 1 if r == self.rows else 0
            elif r == self.rows:
                self.dp[r][c] = 1 if isJoker and self.cmp(r, c + 2) else 0
            else:
                doMatch = self.pattern[c] == '.' or self.pattern[c] == self.str[r]
                
                if isJoker:
                    if (
                        self.cmp(r, c + 2) or
                        doMatch and (
                            self.cmp(r + 1, c + 2) or self.cmp(r + 1, c)
                        ) 
                    ):
                        self.dp[r][c] = 1
                    else:
                        self.dp[r][c] = 0
                else:
                    self.dp[r][c] = doMatch and self.cmp(r + 1, c + 1)
            
        return 1 == self.dp[r][c]
    
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.str = s
        self.pattern = p
        self.rows = len(s)
        self.cols = len(p)
        self.dp = [[-1 for j in range(1 + self.cols)] for i in range(1 + self.rows)]
        self.dp[self.rows][self.cols] = 1
        return self.cmp(0, 0)