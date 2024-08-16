class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        m = len(arrays)
        min_so_far = arrays[0][0]
        max_so_far = arrays[0][-1]
        max_distance = 0
        for array in arrays[1:]:
            current_min = array[0] 
            current_max = array[-1]
            max_distance = max(max_distance, current_max - min_so_far, max_so_far - current_min)
            min_so_far = min(min_so_far, current_min)
            max_so_far = max(max_so_far, current_max)

        return max_distance       