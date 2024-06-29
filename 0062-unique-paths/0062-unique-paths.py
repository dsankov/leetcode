class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0] * n for _ in range(m)]
        matrix[0][0] = 1
        for i in range(m):
            for j in range(n):
                matrix[i][j] += (matrix[i-1][j] if i >= 1 else 0) + (matrix[i][j-1] if j >= 1 else 0)
        return matrix[m-1][n-1]