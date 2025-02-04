class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        highest_bit = 1 << n
        result = []

        for combination in range(highest_bit):
            bit_mask = f"{combination | highest_bit:b}"  
            result.append([nums[idx] for idx, bit in enumerate(bit_mask[1:]) if bit == "1"])
        
        return result