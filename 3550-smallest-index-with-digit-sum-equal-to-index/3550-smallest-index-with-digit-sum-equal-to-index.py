class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for idx, num in enumerate(nums):
            if idx == sum(int(d) for d in str(num)):
                return idx
        return -1