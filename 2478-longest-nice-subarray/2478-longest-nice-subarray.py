class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        used_bits = 0
        max_length = 0
        left = right = 0
        while right < len(nums):
            while used_bits & nums[right] != 0:
                used_bits ^= nums[left]
                left += 1
            used_bits |= nums[right]
            right += 1
            max_length = max(
                max_length, 
                right - left
            )
        return max_length
        