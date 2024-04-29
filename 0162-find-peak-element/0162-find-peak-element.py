class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: 
            return 0
        left, right = 0, n-1
        if nums[left] > nums[left+1]:
            return left
        if nums[right] > nums[right-1]:
            return right
        left += 1
        right -=1
        
        while left <= right:
            medium = (left + right) // 2
            if nums[medium-1] < nums[medium] > nums[medium+1]:
                return medium
            if nums[medium-1] > nums[medium]:
                right = medium - 1
                continue
            if nums[medium] < nums[medium+1]:
                left = medium + 1
                continue
        
        return -1
                