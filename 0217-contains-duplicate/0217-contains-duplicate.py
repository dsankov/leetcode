from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counted_nums = Counter(nums)
        return any([number >= 2 for number in counted_nums.values()])