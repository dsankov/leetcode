class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(num: int) -> int:
            return int("".join(reversed(str(num))))

        result = inf
        seen_reversed = {}
        for idx, num in enumerate(nums):
            if num in seen_reversed:
                result = min(result, idx - seen_reversed[num])
            seen_reversed[reverse(num)] = idx

        return result if result != inf else -1
