class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        start = end = 0
        freqs = defaultdict(int)
        freqs_excess = set()
        max_len = 0
        while end < n:
            freqs[nums[end]] += 1
            if freqs[nums[end]] > k:
                freqs_excess.add(nums[end])

            if not freqs_excess:
                max_len = max(max_len, 1 + end - start)
            else:
                while start < end:
                    freqs[nums[start]] -= 1
                    if freqs[nums[start]] <= k:
                        freqs_excess.discard(nums[start])
                    start += 1
                    if not freqs_excess:
                        max_len = max(max_len, 1 + end - start)
                        break

            end += 1
                
        return max_len

        