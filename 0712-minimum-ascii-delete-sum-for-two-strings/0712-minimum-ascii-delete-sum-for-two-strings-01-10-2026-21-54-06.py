class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = dp[i][j] + ord(s1[i])
                else:
                    dp[i+1][j+1] = max(
                        dp[i][j+1],
                        dp[i+1][j]
                    )
            
        total_cost = sum(ord(ch1) for ch1 in s1 ) + sum(ord(ch2) for ch2 in s2)
        return total_cost - 2 * dp[n][m]

        