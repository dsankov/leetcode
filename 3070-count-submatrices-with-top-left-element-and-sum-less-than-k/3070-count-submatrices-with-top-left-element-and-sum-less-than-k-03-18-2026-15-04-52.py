class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        result = 0
        for row in range(m):
            if row > 0 and grid[row-1][0] > k:
                break
            for col in range(n):
                if row > 0:
                    grid[row][col] += grid[row-1][col]
                if col > 0:
                    grid[row][col] += grid[row][col - 1]
                if row > 0 and col > 0:
                    grid[row][col] -= grid[row-1][col-1]
                if grid[row][col] <= k:
                    result += 1
                else:
                    break
        return result