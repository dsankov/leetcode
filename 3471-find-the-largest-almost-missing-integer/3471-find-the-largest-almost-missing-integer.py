class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freqs = Counter(nums)
        if k == n:
            return max(nums)
        if k == 1:
            max_seen = -1
            for num, freq in reversed(freqs.most_common()):
                if freq > 1:
                    break
                max_seen = max(max_seen, num)
            return max_seen
       
        return max(num if freqs[num] == 1 else -1 for num in [nums[0], nums[-1]])
        