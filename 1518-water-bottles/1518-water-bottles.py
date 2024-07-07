class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = 0
        empty_bottles = 0
        while numBottles:
            result += numBottles
            empty_bottles, numBottles = (empty_bottles + numBottles) % numExchange, (empty_bottles + numBottles) // numExchange
        return result