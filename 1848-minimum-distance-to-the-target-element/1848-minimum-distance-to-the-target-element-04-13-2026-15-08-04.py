class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        if nums[start] == target:
            return 0
        for d in range(1, max(start + 1, n - start)):
            if start + d < n and nums[start + d] == target:
                return d 
            if start - d >= 0 and nums[start - d] == target:
                return d
        return -1