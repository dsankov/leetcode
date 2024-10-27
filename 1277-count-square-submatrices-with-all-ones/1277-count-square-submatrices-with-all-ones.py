class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        result = 0
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 1:
                    dp[row + 1][col + 1] = 1 + min(
                        dp[row][col + 1],
                        dp[row][col],
                        dp[row + 1][col]
                    )
                result += dp[row + 1][col + 1]
        return result
    