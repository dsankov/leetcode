class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 0
        dp0 = [0] * (n + 1)
        dp1 = [0] * (n + 1)
        for col in range(1, n):
            new_dp0 = [0] * (n + 1)
            new_dp1 = [0] * (n + 1)
            for row in range(n + 1):
                prev = 0
                curr = sum(grid[_][col] for _ in range(row))
                for i in range(n + 1):
                    if i > 0 and i <= row:
                        curr -= grid[i - 1][col]
                    if col > 0 and i > row:
                        prev += grid[i - 1][col - 1]
                    new_dp0[i] = max(new_dp0[i], prev + dp0[row], dp1[row])
                    new_dp1[i] = max(new_dp1[i], curr + dp1[row], curr + prev + dp0[row])
            dp0, dp1 = new_dp0, new_dp1
        return max(dp1)        