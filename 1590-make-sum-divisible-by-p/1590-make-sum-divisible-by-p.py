class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        total_sum = 0
        for num in nums:
            total_sum = (total_sum + num) % p
        if total_sum == 0:
            return 0
        mod_map = {0: -1}
        min_len = n
        prefix_sum = 0
        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p
            needed_sum = (prefix_sum - total_sum) % p
            if needed_sum in mod_map:
                min_len = min(min_len, i - mod_map[needed_sum]) 
            mod_map[prefix_sum] = i
        return min_len if min_len != n else -1
        