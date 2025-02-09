class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        bad_pairs = 0
        diff_freqs = defaultdict(int)

        for idx, num in enumerate(nums):
            diff = idx - num
            good_pairs = diff_freqs[diff]
            bad_pairs += idx - good_pairs
            diff_freqs[diff] += 1

        return bad_pairs
        