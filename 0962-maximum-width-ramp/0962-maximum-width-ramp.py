class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        indices_stack = []

        for index, num in enumerate(nums):
            if not indices_stack or nums[indices_stack[-1]] > num:
                indices_stack.append(index)
        max_ramp_width = 0

        for right in range(n-1, -1, -1):
            while indices_stack and nums[indices_stack[-1]] <= nums[right]:
                max_ramp_width = max(max_ramp_width, right - indices_stack[-1])
                indices_stack.pop()

        return max_ramp_width