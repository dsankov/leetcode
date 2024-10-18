class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.n = len(nums)
        self.nums = nums
        self.total_or = 0
        for num in nums:
            self.total_or |= num
        self.UNKNOWN = -1
        self.computed_results = defaultdict(lambda: self.UNKNOWN)
        return self.max_or_subset(0, 0)
    def max_or_subset(self, num_index: int, current_or: int) -> int:
        if num_index >= self.n:
            return 1 if current_or == self.total_or else 0
        if self.computed_results[(num_index, current_or)] != self.UNKNOWN:
            return self.computed_results[(num_index, current_or)]
        with_or = self.max_or_subset(num_index+1, current_or | self.nums[num_index])
        without_or = self.max_or_subset(num_index+1, current_or)
        self.computed_results[(num_index, current_or)] = with_or + without_or
        return with_or + without_or
        