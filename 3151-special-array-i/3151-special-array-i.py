class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return not any((a + b) % 2 == 0 for a, b in zip(nums[:-1], nums[1:]))
            
