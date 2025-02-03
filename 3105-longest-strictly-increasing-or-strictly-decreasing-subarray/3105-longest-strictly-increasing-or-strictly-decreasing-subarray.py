class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        prev_num = nums[0]
        inc_strike = dec_strike = 1
        max_inc_strike = max_dec_strike = 1
        for num in nums[1:]:
            if num > prev_num:
                inc_strike += 1
                dec_strike = 1
            elif num < prev_num:
                dec_strike += 1
                inc_strike = 1
            else:
                inc_strike = dec_strike = 1
            max_inc_strike = max(max_inc_strike, inc_strike)
            max_dec_strike = max(max_dec_strike, dec_strike)
            prev_num = num
        return max(max_inc_strike, max_dec_strike)
        