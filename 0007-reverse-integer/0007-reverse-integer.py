class Solution:
    def reverse(self, x: int) -> int:
        num_str = str(x)
        if num_str[0] == "-":
            sign = -1
            num_str = num_str[:0:-1]
        else:
            sign = 1
            num_str = num_str[::-1]
        reversed_x = int(num_str)
        if reversed_x > 2**31:
            return 0
        return sign * reversed_x