class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        left, middle, right = 0b11110000, 0b00111100, 0b00001111
        occupied = collections.defaultdict(int)
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                occupied[row] |= 1 << (seat - 2)

        ans = (n - len(occupied)) * 2
        for row, bitmask in occupied.items():
            if (
                (bitmask & left) == 0
                or (bitmask & middle) == 0
                or (bitmask & right) == 0
            ):
                ans += 1
        return ans
        