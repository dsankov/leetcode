class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        shift = left
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[(mid + shift) % n]:
                return (mid + shift) % n
            if target > nums[(mid + shift) % n]:
                left = mid + 1
            else:
                right = mid - 1

        return -1