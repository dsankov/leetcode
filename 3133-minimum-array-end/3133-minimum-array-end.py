class Solution:
    def minEnd(self, n: int, x: int) -> int:
        shift_counter = 0
        n -= 1
        result = x
        while n > 0:
            if not (x & (1 << shift_counter)):
                mask_bit = n & 1
                result |= (mask_bit << shift_counter)
                n >>= 1
            shift_counter += 1 
        return result

        