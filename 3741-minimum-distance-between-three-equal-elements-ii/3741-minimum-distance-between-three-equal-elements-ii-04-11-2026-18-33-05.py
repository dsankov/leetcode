class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        prevs = defaultdict(lambda: [-1, -1])
        result = inf

        for idx, num in enumerate(nums):
            prev, grand_prev = prevs[num]
            if grand_prev >= 0:
                result = min(result, (idx - grand_prev) * 2)
            prevs[num] = [idx, prev]

        return result if result != inf else -1
        