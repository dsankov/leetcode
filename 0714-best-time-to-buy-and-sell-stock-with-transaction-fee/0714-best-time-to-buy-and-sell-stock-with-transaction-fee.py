class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0
        empty_case = 0
        hold_case = -prices[0]
        for price in prices[1:]:
            empty_case, hold_case = max(empty_case, hold_case + price - fee ),  max(hold_case, empty_case - price)
            
        return max(hold_case, empty_case)
        