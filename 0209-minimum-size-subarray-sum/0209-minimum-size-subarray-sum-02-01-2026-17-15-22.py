class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = right = 0
        cur_sum = 0
        min_len = inf

        while left < n:
            while right < n and cur_sum < target:
                cur_sum += nums[right]
                right += 1
            if cur_sum < target and right >= n:
                break

            while cur_sum >= target and left < n:
                min_len = min(min_len, right - left )
                cur_sum -= nums[left]
                left += 1
            

        return min_len if min_len < inf else 0