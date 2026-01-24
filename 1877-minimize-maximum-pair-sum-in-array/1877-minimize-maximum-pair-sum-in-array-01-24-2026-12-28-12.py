class Solution:
    def minPairSum(self, nums: List[int]) -> int:
       n = len(nums)
       nums.sort() 
    #    print(nums)

       return max(nums[i] + nums[n - 1 - i] for i in range(n // 2))