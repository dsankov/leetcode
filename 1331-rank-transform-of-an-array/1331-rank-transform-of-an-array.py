class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        return [dict(zip(sorted(set(arr)), count(1)))[num] for num in arr]
        