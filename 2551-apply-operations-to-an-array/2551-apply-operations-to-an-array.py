class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        write_idx = 0
        result = [0] * n
        for i in range(n - 1):
            if nums[i] == 0:
                continue
            if nums[i] == nums[i+1]:
                result[write_idx] = nums[i] * 2
                nums[i+1] = 0
            else:
                result[write_idx] = nums[i]

            write_idx += 1

        result[write_idx] = nums[n-1]
        return result
        