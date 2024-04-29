class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n, m = len(spells), len(potions)
        pairs = [0] * n
        potions.sort()
        for i, spell in enumerate(spells):
            left, right = 0, m - 1
            while left <= right:                
                medium = (left + right) // 2
                if spells[i] * potions[medium] >= success:
                    right = medium - 1
                else:
                    left = medium + 1
            pairs[i] = m - left
        return pairs