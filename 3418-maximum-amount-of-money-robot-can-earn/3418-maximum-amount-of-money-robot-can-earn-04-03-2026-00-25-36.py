from functools import cache


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        dp = [[[-inf] * 3 for col in range(n)] for row in range(m)]

        dp[0][0][0] = coins[0][0]
        dp[0][0][1] = max(0, dp[0][0][0])
        dp[0][0][2] = max(0, dp[0][0][1])

        for col in range(1, n):
            dp[0][col][0] = coins[0][col] + dp[0][col - 1][0]
            dp[0][col][1] = max(
                max(0, coins[0][col]) + dp[0][col - 1][0],
                coins[0][col] + dp[0][col - 1][1],
            )
            dp[0][col][2] = max(
                max(0, coins[0][col]) + dp[0][col - 1][1],
                coins[0][col] + dp[0][col - 1][2],
            )
        for row in range(1, m):
            dp[row][0][0] = coins[row][0] + dp[row - 1][0][0]
            dp[row][0][1] = max(
                max(0, coins[row][0]) + dp[row - 1][0][0],
                coins[row][0] + dp[row - 1][0][1],
            )
            dp[row][0][2] = max(
                max(0, coins[row][0]) + dp[row - 1][0][1],
                coins[row][0] + dp[row - 1][0][2],
            )

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col][0] = coins[row][col] + max(
                    dp[row - 1][col][0], dp[row][col - 1][0]
                )
                dp[row][col][1] = max(
                    max(0, coins[row][col])
                    + max(dp[row - 1][col][0], dp[row][col - 1][0]),
                    coins[row][col] + max(dp[row - 1][col][1], dp[row][col - 1][1]),
                )
                dp[row][col][2] = max(
                    max(0, coins[row][col])
                    + max(dp[row - 1][col][1], dp[row][col - 1][1]),
                    coins[row][col] + max(dp[row - 1][col][2], dp[row][col - 1][2]),
                )

        return dp[m-1][n-1][2]

        # @cache
        # def max_amount(r, c, a):
        #     if r == m-1 and c == n-1:
        #         if coins[r][c] >= 0 or a == 0:
        #             return(coins[r][c])
        #         else:
        #             return 0
        #     if r >= m or c >= n:
        #         return -inf

        #     dont_use_ammo = coins[r][c] + max(
        #             max_amount(r+1, c, a),
        #             max_amount(r, c+1, a)
        #         )
        #     if coins[r][c] >= 0 or a == 0:
        #         return dont_use_ammo

        #     use_ammo = max(
        #             max_amount(r+1, c, a-1),
        #             max_amount(r, c+1, a-1)
        #         )

        #     return max(use_ammo, dont_use_ammo)
