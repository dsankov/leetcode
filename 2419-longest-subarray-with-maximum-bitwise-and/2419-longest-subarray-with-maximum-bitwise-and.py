class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = 0
        cur_strike = 0
        result = 0
        for num in nums:
            if num > max_num:
                max_num = num
                cur_strike = 0
                result = 0
            if num == max_num:
                cur_strike += 1
                result = max(result, cur_strike)
            else:
                cur_strike = 0

        return result
        