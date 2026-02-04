class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        down_subs: list[tuple[int, int, int]] = []

        sub_start = 0
        cur_sum = nums[0]

        for i in range(1, n):
            if nums[i - 1] <= nums[i]:
                down_subs.append((sub_start, i - 1, cur_sum))
                sub_start = i
                cur_sum = 0
            cur_sum += nums[i]

        down_subs.append((sub_start, n - 1, cur_sum))

        max_end_at = [0] * n
        for i in range(n):
            max_end_at[i] = nums[i]
            if i > 0 and nums[i - 1] < nums[i] and max_end_at[i - 1] > 0:
                max_end_at[i] += max_end_at[i - 1]

        max_start_at = [0] * n
        for i in range(n - 1, -1, -1):       
            max_start_at[i] = nums[i]
            if i < n - 1 and nums[i] < nums[i + 1] and max_start_at[i + 1] > 0:
                max_start_at[i] += max_start_at[i + 1]

        result = -inf
        for sub_start, sub_end, sub_sum in down_subs:
            if (sub_start < sub_end and
                sub_start > 0 and nums[sub_start - 1] < nums[sub_start] and
                sub_end < n - 1 and nums[sub_end] < nums[sub_end + 1]
                ):
                    result = max(result,
                                            max_end_at[sub_start - 1] 
                                            + sub_sum 
                                            + max_start_at[sub_end + 1]
                                            )
                                            
        return result