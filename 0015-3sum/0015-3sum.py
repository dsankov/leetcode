class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = set()
        for i in range(n - 2):
            j = i +1
            k = n - 1
            while j < k:
                test_sum = nums[i] + nums[j] + nums[k]
                if test_sum == 0:
                    result.add(tuple(sorted((nums[i],nums[j],nums[k]))))
                    j += 1
                    k -= 1
            
                elif test_sum < 0:
                    j += 1
                else: # test_sum > 0
                    k -= 1

        return list(result)