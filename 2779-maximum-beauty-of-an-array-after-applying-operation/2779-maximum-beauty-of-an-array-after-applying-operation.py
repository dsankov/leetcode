class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        left, right = 0, 0
        max_length = 0
        while left < n:
            while right+1 < n and nums[right+1] - nums[left] <= 2 * k:
                right += 1
            max_length = max(max_length, right - left + 1)
            # while left < n and nums[right] - nums[left] <= 2 * k:
            left += 1
        return max_length