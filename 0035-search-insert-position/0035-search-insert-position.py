class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        if target < nums[left]:
            return left
        if target > nums[right]:
            return right + 1

        while left <= right:
            # print(f"{left=}->{nums[left]}\t{right=}->{nums[right]}")
            if target == nums[right]:
                return right
            if target == nums[left]:
                return left
            middle = (left + right + 1) // 2
            # print(f"{middle=}->{nums[middle]}")
            if target > nums[middle]:
                left = middle + 1
            elif target < nums[middle]:
                right = middle - 1
            else:
                return middle
        return right + 1 

        