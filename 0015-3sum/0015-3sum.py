class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []
        for i in range(n - 2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            j = i +1
            k = n - 1
            while j < k:
                test_sum = nums[i] + nums[j] + nums[k]
                if test_sum > 0:
                    k -= 1
                elif test_sum < 0:
                    j += 1
                else: # test_sum == 0
                    result.append((nums[i],nums[j],nums[k]))
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        return result