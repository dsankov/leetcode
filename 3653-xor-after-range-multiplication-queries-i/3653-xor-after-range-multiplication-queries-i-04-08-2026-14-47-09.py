from functools import reduce
from operator import xor

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MODULO = 10 ** 9 + 7
        for l, r, k, v in queries:
            for i in range(l, r+1, k):
                nums[i] = (nums[i] * v) % MODULO
        return reduce(xor, nums)
