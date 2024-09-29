class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        prices_iter = iter(prices)
        buy_price = next(prices_iter)
        for price in prices_iter:
            max_profit = max(max_profit, price - buy_price)
            buy_price = min(buy_price, price)
        return max_profit

        