#https://leetcode.com/problems/solving-questions-with-brainpower/description/

class Solution:
    def mostPoints(self, questions) -> int:
        n = len(questions)
        points = [0] * n
        
        points[n - 1] = questions[n - 1][0]
        for step in range(n - 2, -1, -1):
            pay = questions[step][0]
            jump = step + questions[step][1] + 1
            points[step] = max(points[step + 1], pay + (0 if jump >= n else points[jump]))
        
        return points[0]