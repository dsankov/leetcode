class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        min_diff = math.inf
        for i in range(n - (k - 1)):
            cur_diff = nums[i + (k - 1)] - nums[i]
            min_diff = min(min_diff, cur_diff)

        return min_diff
        