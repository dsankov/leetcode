class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        prev_num = cur_sum = max_sum = nums[0]
        for num in nums[1:]:
            if num > prev_num:
                cur_sum += num
            else:
                cur_sum = num
            max_sum = max(max_sum, cur_sum)
            prev_num = num
        return max_sum
        