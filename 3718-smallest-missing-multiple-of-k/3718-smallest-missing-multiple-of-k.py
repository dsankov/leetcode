class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        mult = 1
        while True:
            if mult * k not in nums:
                return mult * k
            mult += 1 
        