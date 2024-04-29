class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n, m = len(spells), len(potions)
        pairs = [0] * n
        potions.sort()
        for i, spell in enumerate(spells):
            potion_position_than_exeed_success_product = bisect.bisect_left(potions, math.ceil(success / spell))
            pairs[i] = m - potion_position_than_exeed_success_product
        return pairs