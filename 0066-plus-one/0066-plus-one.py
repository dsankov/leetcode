class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        result = [0] * (n + 1)
        ptr = 0
        transit = 0
        digits = digits[::-1]
        digits[0] += 1
        while ptr < n:
            result[ptr] = (digits[ptr] + transit) % 10
            transit = (digits[ptr] + transit) // 10
            ptr += 1

        if transit > 0:
            result[ptr] = transit
            return result[::-1]

        return result[-2::-1]
        