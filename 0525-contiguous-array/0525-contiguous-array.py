class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_ones = [nums[0]]
        for num in nums[1:]:
            prefix_ones.append(prefix_ones[-1] + num)

        deltas = {0: -1}
        max_len = 0
        for pos, num in enumerate(nums):
            ones = prefix_ones[pos]
            zeroes = pos + 1 - ones
            delta = zeroes - ones
            if delta in deltas:
                max_len = max(max_len, pos - deltas[delta])
            else:
                deltas[delta] = pos



        return max_len