class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return list(map(int, chain.from_iterable(str(num) for num in nums)))
        