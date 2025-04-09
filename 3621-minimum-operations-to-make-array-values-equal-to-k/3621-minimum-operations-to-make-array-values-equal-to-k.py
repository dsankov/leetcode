class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        larger_nums = set()
        for num in nums:
            if num < k:
                return -1
            if num > k:
                larger_nums.add(num)

        return len(larger_nums)