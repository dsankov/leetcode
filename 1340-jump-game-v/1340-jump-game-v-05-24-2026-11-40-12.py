class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        memo = [-1] * n
        def dp(idx):
            if memo[idx] != -1:
                return memo[idx]
            cur_max = 0
            for dd in range(1, 1 + min(idx, d)):
                if not arr[idx - dd] < arr[idx]:
                    break 
                cur_max = max(cur_max, dp(idx - dd))
            for dd in range(1, 1 + min(n - 1 - idx, d)):
                if not arr[idx + dd] < arr[idx]:
                    break 
                cur_max = max(cur_max, dp(idx + dd))
            memo[idx] = cur_max + 1
            return memo[idx]
        return max(dp(start) for start in range(n))
        