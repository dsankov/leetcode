class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_max = [0] * n
        suffix_max = [0] * n
        prefix_max[0] = nums[0]
        suffix_max[-1] = nums[-1]
        for beg_idx in range(1, n):
            end_idx = n - 1 - beg_idx
            prefix_max[beg_idx] = max(prefix_max[beg_idx - 1], nums[beg_idx])
            suffix_max[end_idx] = max(suffix_max[end_idx + 1], nums[end_idx])
        
        max_value = 0
        for mid_idx in range(1, n-1):
            max_value = max(max_value, (prefix_max[mid_idx - 1] - nums[mid_idx]) * suffix_max[mid_idx + 1])

        return max_value
        