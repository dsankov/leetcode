class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # ''' bruteforce. time is O(n^2)'''

        # max_sum = float('-inf')
        # for start in range(len(nums)):
        #     for end in range(start+1, len(nums)+1):
        #         sum_of_slice = sum(nums[start:end])
        #         max_sum = max(max_sum, sum_of_slice)
        # return max_sum

        sliding_sum = 0
        max_subarray_sum = float('-inf')
        for number in nums:
            sliding_sum += number
            max_subarray_sum = max(max_subarray_sum, sliding_sum)
            sliding_sum = max(0, sliding_sum)


        return max_subarray_sum







