class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return sum(int(digit) for digit in f"{(start ^ goal):b}")
