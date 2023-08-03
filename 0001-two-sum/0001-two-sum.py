class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tested_nums = {}
        for index, number in enumerate(nums):
            if target - number in tested_nums:
                return (index, tested_nums[target - number])
            else:
                tested_nums[number] = index
        
        return [] # error case