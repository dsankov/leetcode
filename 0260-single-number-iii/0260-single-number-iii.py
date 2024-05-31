class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        total_xor = 0
        for num in nums:
            total_xor ^= num
        mask = total_xor & (-total_xor) # first set bit from right
        answer = 0
        for num in nums:
            if num & mask:
                answer ^= num
        return answer, answer ^ total_xor
        