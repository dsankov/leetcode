class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def count_less(value: int):
            left = 0
            right = len(nums) - 1
            result = 0
            while left < right:
                if nums[left] + nums[right] >= value:
                    right -= 1
                else:
                    result += right - left
                    left += 1
            return result

        nums.sort()
        return count_less(upper+1) - count_less(lower)
        