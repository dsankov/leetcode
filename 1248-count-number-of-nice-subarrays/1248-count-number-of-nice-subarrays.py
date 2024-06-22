class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        last_seen_odd_index = -1
        segments = []
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                segments.append(i - last_seen_odd_index)
                last_seen_odd_index = i
        segments.append(len(nums) - last_seen_odd_index)
        result = 0
        for i in range(len(segments) - k):
            result += segments[i] * segments[i+k]
        return result
