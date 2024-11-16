class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        
        def permutations(start):
            if start == n - 1:
                result.append(nums.copy())
                return
            permutations(start + 1)
            for swap_index in range(start + 1, n):
                nums[start], nums[swap_index] = nums[swap_index], nums[start]
                permutations(start + 1)
                nums[start], nums[swap_index] = nums[swap_index], nums[start]

        permutations(0)
        return result


