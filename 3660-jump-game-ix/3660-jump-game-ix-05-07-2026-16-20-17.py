class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        max_to_left = [0] * n
        min_to_right = [0] * n
        max_to_left[0] = nums[0]
        min_to_right[-1] = nums[-1]
        for i in range(1, n):
            j = n - 1 - i
            max_to_left[i] = max(max_to_left[i - 1], nums[i])
            min_to_right[j] = min(min_to_right[j + 1], nums[j])

        result = [0] * n
        result[-1] = max_to_left[-1]
        for i in range(n - 2, -1, -1):
            if max_to_left[i] > min_to_right[i + 1]:
                result[i] = result[i+1]
            else:
                result[i] = max_to_left[i]

        return result