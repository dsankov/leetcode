class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        seen_max_len = 0
        left = right = 0

        while left < n and right < n:
            while right < n - 1 and nums[left] * k >= nums[right + 1]:
                right += 1
            seen_max_len = max(seen_max_len, 1 + right - left)
            if right == n - 1:
                break

            right += 1
            while left < n  and nums[left ] * k  < nums[right]:
                left += 1
        return n - seen_max_len