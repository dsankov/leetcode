class Solution:
    def countInterestingSubarrays(
        self, nums: List[int], modulo: int, k: int
    ) -> int:
        interesting_nums_counts = defaultdict(int)
        interesting_nums_counts[0] = 1
        result = 0
        prefix_interesting_nums_count = 0
        for i in range(len(nums)):
            prefix_interesting_nums_count += 1 if nums[i] % modulo == k else 0
            result += interesting_nums_counts[(prefix_interesting_nums_count - k + modulo) % modulo]
            interesting_nums_counts[prefix_interesting_nums_count % modulo] += 1
        return result