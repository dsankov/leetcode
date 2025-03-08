class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        left = right = 0
        min_swaps = float("inf")
        count_swaps = 0

        while right < n:
            while right < n and right - left < k:
                if blocks[right] == "W":
                    count_swaps += 1
                right += 1
            min_swaps = min(min_swaps, count_swaps)
            if blocks[left] == "W":
                count_swaps -= 1
            left += 1
        return min_swaps