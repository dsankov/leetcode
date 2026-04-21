class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        lo, hi = 0, n - 1
        while lo < hi:
            cur_sum = nums[lo] + nums[hi]
            if cur_sum < target or (lo > 0 and nums[lo - 1] == nums[lo]):
                lo += 1
            elif cur_sum > target or (hi < n - 1 and nums[hi + 1] == nums[hi]):
                hi -= 1
            else:
                return [lo+1, hi+1]
        