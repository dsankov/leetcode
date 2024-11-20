class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        def rec(index: int) -> List[List[int]]:
            subsets = []
            if index >= n:
                return [[]]
            subsets.extend(rec(index + 1))
            subsets.extend([nums[index]] + subset for subset in rec(index + 1))

            return subsets
        
        return rec(0)