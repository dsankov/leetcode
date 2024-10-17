class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        n = len(digits)
        max_digit_index = n-1
        swap_source, swap_dest = -1, -1
        for i in range(n-1, -1, -1):
            if digits[i] > digits[max_digit_index]:
                max_digit_index = i
            elif digits[i] < digits[max_digit_index]:
                swap_source, swap_dest = i, max_digit_index
        if swap_source == -1:
            return num
        digits[swap_source], digits[swap_dest] = digits[swap_dest], digits[swap_source]
        return int("".join(digits))
        