from functools import reduce 
import operator
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        all_bits = (1 << maximumBit) - 1
        total_xor = reduce(operator.xor, nums)
        result = [
            tail_xor ^ all_bits 
            for tail_xor in accumulate(nums[:0:-1], operator.xor, initial=total_xor)
            ]
        return result
        