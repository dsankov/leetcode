class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_bit = 0
        mask = 1
        for bit_index in range(24):
            cur_bit = 0
            for num in candidates:
                if num & mask:
                    cur_bit += 1
            max_bit = max_bit if max_bit > cur_bit else cur_bit
            mask <<= 1

        return max_bit
        