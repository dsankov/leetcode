class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        result = 0
        for num in nums[:-1]:
            left_sum += num
            right_sum -= num
            if left_sum >= right_sum:
                result += 1
        return result
        