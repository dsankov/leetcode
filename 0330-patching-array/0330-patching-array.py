class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        max_patched = 0
        number_of_patches = 0
        i = 0
        while i < len(nums):
            if max_patched >= n:
                return number_of_patches
            if max_patched >= nums[i] - 1:
                max_patched += nums[i]
                i += 1
                continue
            
            # max_patched < nums[i] - 1
            number_of_patches += 1
            max_patched += max_patched + 1

        while max_patched < n:
            number_of_patches += 1
            max_patched += max_patched + 1
        return number_of_patches

            
            

        