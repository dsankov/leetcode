class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        nums = set(range(1, len(grid)**2 + 1))
        for num in itertools.chain.from_iterable(grid):
            if num not in nums:
                a = num
            else:
                nums.remove(num)
        b = next(iter(nums))
        return [a, b]
