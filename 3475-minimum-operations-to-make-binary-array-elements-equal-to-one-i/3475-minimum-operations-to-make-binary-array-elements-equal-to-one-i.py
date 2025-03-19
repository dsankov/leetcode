class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations_count = 0
        for start_pos in range(len(nums) - 2):
            if nums[start_pos] == 0:
                operations_count += 1
                nums[start_pos + 0] = 1
                nums[start_pos + 1] ^= 1
                nums[start_pos + 2] ^= 1
        if nums[-2] == 1 and nums[-1] == 1:
            return operations_count
        return -1
        