class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = nums[0]
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                prefix_sum += nums[i]
            else:
                break
        nums = set(nums)
        while prefix_sum in nums:
            prefix_sum += 1
        return prefix_sum
        