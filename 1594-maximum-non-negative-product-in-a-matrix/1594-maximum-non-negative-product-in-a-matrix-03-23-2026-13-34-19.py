class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pos_dp = [[-1] * (n + 1) for _ in range(m + 1)]
        neg_dp = [[-1] * (n + 1) for _ in range(m + 1)]

        pos_dp[0][1] = 1
        # neg_dp[0][1] = 1

        # for col in range(1, n):
        #     if grid[0][col] >= 0:
        #         pos_pd[0][col]
        def print_grid(mat):
            for line in mat:
                print(line)

        for row in range(m):
            print_grid(pos_dp)
            print("---")
            for col in range(n):
                if grid[row][col] >= 0:
                    pos_dp[row + 1][col + 1] = grid[row][col] * max(
                        pos_dp[row][col + 1], pos_dp[row + 1][col]
                    )
                    neg_dp[row + 1][col + 1] = grid[row][col] * max(
                        neg_dp[row][col + 1], neg_dp[row + 1][col]
                    )
                else:
                    neg_dp[row + 1][col + 1] = -grid[row][col] * max(
                        pos_dp[row][col + 1], pos_dp[row + 1][col]
                    )
                    pos_dp[row + 1][col + 1] = -grid[row][col] * max(
                        neg_dp[row][col + 1], neg_dp[row + 1][col]
                    )
        return pos_dp[m][n] % (10**9 + 7) if pos_dp[m][n] >=0 else -1
            
