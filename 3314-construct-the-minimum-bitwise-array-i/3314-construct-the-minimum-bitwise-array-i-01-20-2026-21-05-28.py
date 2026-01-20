class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num % 2 == 0:
                ans.append(-1)
            else:
                ans.append(
                    num ^
                    (~num & (num + 1)) >> 1
                 )
        return ans