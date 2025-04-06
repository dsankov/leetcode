class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [1] * n
        idx_of_max_divisor = [-1] * n
        idx_of_longest_tail = 0

        for num_idx in range(1, n):
            for potential_factor_idx in range(num_idx):
                if nums[num_idx] % nums[potential_factor_idx] == 0 and dp[num_idx] < dp[potential_factor_idx] + 1:
                    dp[num_idx] = dp[potential_factor_idx] + 1
                    idx_of_max_divisor[num_idx] = potential_factor_idx
                if dp[num_idx] > dp[idx_of_longest_tail]:
                    idx_of_longest_tail = num_idx

        result = []
        num_idx = idx_of_longest_tail
        while num_idx >= 0:
            result.append(nums[num_idx])
            num_idx = idx_of_max_divisor[num_idx]
        return result

        