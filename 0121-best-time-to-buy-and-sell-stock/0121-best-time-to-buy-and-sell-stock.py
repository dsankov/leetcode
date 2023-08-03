

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for current_price in prices:
            min_price = min(min_price, current_price)
            current_profit = current_price - min_price
            max_profit = max(max_profit, current_profit)

        return max_profit
        
        