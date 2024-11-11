class StockSpanner:

    def __init__(self):
        self.prices_stack = []  # (price, day)
        self.today = 0
        

    def next(self, price: int) -> int:
        passed_day = self.today
        while self.prices_stack and self.prices_stack[-1][0] <= price:
            _former_price, passed_day = self.prices_stack.pop()
        self.prices_stack.append((price, passed_day))
        self.today += 1
        return self.today - passed_day
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)