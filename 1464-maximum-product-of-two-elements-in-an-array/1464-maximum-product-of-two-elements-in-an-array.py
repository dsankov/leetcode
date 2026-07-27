class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_1 = max_2 = 0
        for num in nums:
            if max_1 < num:
                max_2 = max_1
                max_1 = num
            elif max_2 < num:
                max_2 = num
        return (max_1 - 1) * (max_2 - 1)
        