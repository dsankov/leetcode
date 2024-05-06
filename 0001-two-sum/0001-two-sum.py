class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        differences = {}
        for i in range(n):
            x = nums[i]
            if x in differences:
                return  i, differences[x]
            differences[target-x] = i