class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        modulo = 10**9 + 7
        dp = [1] + [0] * (high)
        for i in range(1, len(dp)):
            if i >= zero:
                dp[i] += dp[i - zero]
            if i >= one:
                dp[i] += dp[i - one]

            dp[i] %= modulo
        return sum(dp[low:high+1]) % modulo