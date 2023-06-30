class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        i = 1
        while i < n + 1:
            result[i] = result[i >> 1] + i % 2
            i += 1
        return result