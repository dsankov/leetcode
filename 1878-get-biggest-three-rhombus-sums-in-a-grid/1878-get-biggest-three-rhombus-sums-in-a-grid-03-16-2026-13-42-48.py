class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        rhombus_sums = []

        for row in range(m):
            for col in range(n):
                rhombus_sums.append(grid[row][col])
                max_size = min(col, n - 1 - col, (m - 1 - row) // 2 )
                for size in range(1, max_size + 1):
                    rhombus_sum = (
                        grid[row][col] + 
                        grid[row + size][col - size] +
                        grid[row + size][col + size] +
                        grid[row + 2 * size][col]
                    )
                    for d in range(1, size):
                        rhombus_sum += (
                            grid[row+d][col+d] +
                            grid[row+d][col-d] + 
                            grid[row+size-d][col+d] +
                            grid[row+size-d][col-d]
                        )
                    rhombus_sums.append(rhombus_sum)

        rhombus_sums = sorted(set(rhombus_sums), reverse=True)
        return rhombus_sums[:3]

        