class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        m = len(arrays)
        min_so_far = min(arrays[0])
        max_so_far = max(arrays[0])
        max_distance = 0
        for i in range(1, m):
            current_min = min(arrays[i]) 
            current_max = max(arrays[i])
            max_distance = max(max_distance, abs(min_so_far - current_max), abs(max_so_far - current_min))
            min_so_far = min(min_so_far, current_min)
            max_so_far = max(max_so_far, current_max)

        return max_distance       