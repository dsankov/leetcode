class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        shift_mask = n ^ (n >> 1)
        return shift_mask & (shift_mask + 1) == 0