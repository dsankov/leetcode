class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while (right - left > 1):
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle
            elif nums[middle] < target:
                left = middle
            else:
                return middle
     
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        else:
            return -1
        