class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        for i in range(1, amount + 1):
            dp[i] = 1 + min(
                dp[i - coin] if i >= coin else inf for coin in coins 
            )
        return dp[-1] if dp[-1] != inf else -1
        