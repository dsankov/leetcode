class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        same_at_left = [0] * n
        same_at_right = [0] * n
        num_to_pos = {}
        for idx in range(-n, n):
            num = nums[idx % n]
            if idx >= 0:
                same_at_left[idx] = num_to_pos[num]
            num_to_pos[num] = idx       

        num_to_pos.clear()
        for idx in range(2 * n - 1, -1, -1):
            num = nums[idx % n]
            if idx < n:
                same_at_right[idx] = num_to_pos[num]
            num_to_pos[num] = idx 

        result = []
        for idx in queries:

            d = min(idx - same_at_left[idx], same_at_right[idx] - idx)
            result.append(d if d < n else -1)
        return result