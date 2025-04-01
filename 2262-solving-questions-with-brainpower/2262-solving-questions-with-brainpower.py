class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        dp[-1] = questions[-1][0]
        for i in range(n - 2, -1, -1):
            points, brainpower = questions[i]
            if i + brainpower + 1 < n:
                dp[i] = max(dp[i + 1], points + dp[i + brainpower + 1])
            else:
                dp[i] = max(dp[i + 1], points)
        return dp[0]
        