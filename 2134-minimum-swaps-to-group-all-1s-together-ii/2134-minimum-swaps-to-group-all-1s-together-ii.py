class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_ones = sum(nums)
        ones_count = sum(nums[:total_ones])
        minimum_swaps = total_ones - ones_count
        end = total_ones
        for start in range(1, len(nums)):
            ones_count -= nums[start - 1]
            ones_count += nums[end % len(nums)]
            end += 1
            minimum_swaps = min(minimum_swaps, total_ones - ones_count)

        return minimum_swaps