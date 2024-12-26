class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        prev = defaultdict(int)
        prev[0] = 1

        for num in nums:
            curr = defaultdict(int)
            for prev_sum, num_of_expressions in prev.items():
                curr[prev_sum + num] += num_of_expressions
                curr[prev_sum - num] += num_of_expressions
            prev = curr

        return curr[target]
        