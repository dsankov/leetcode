class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        distinct_count = len(set(nums))
        current_seen_nums = defaultdict(int)
        left, right = 0, 0
        result = 0
        while right < n:
            current_seen_nums[nums[right]] += 1
            if len(current_seen_nums) == distinct_count:
                right_range = n - right
                while len(current_seen_nums) == distinct_count:
                    result += right_range
                    current_seen_nums[nums[left]] -= 1
                    if current_seen_nums[nums[left]] == 0:
                        del(current_seen_nums[nums[left]])
                    left += 1
            right += 1

        return result
                