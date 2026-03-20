class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        result = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for row in range(m - k + 1):
            for col in range(n - k + 1):
                submatrix_values = sorted(
                    set(
                        [
                            grid[i][j]
                            for i in range(row, row + k)
                            for j in range(col, col + k)
                        ]
                    )
                )
                if (num_values := len(submatrix_values)) == 1:
                    result[row][col] = 0
                else:
                    result[row][col] = min(
                        abs(submatrix_values[i + 1] - submatrix_values[i])
                        for i in range(num_values - 1)
                    )

        return result
