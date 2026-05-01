class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        f0 = sum(i * num for i, num in enumerate(nums))
        max_f = f0
        cur_f = f0
        for num in nums[:-1]:
            cur_f = cur_f - total_sum + num * n
            max_f = max(max_f, cur_f)
        return max_f 