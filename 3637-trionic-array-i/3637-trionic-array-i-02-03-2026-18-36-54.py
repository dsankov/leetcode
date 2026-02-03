class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        while i < n - 1 and nums[i] < nums[i+1]:
            i += 1
        p = i
        if p == 0:
            return False

        while i < n - 1 and nums[i] > nums[i+1]:
            i += 1
        q = i
        if q == p or q == n-1:
            return False 

        while i < n - 1:
            if nums[i] >= nums[i+1]:
                return False
            i += 1

        return True

        