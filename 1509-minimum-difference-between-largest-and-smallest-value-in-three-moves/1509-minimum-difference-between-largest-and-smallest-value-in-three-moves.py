class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        min_4 = sorted(heapq.nsmallest(4, nums))
        max_4 = sorted(heapq.nlargest(4, nums))
        min_diff = inf
        for i in range(4):
            min_diff = min(min_diff, max_4[i] - min_4[i])
        return min_diff