class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights_ascending_queue = deque() # idx, height
        max_area = 0
        for curr_idx, curr_height in enumerate(heights):
            right_max_idx = curr_idx
            while heights_ascending_queue and heights_ascending_queue[-1][1] >= curr_height:
                prev_max_idx, prev_max_height = heights_ascending_queue.pop()
                max_area = max(max_area, prev_max_height * (curr_idx - prev_max_idx))
                right_max_idx = prev_max_idx

            heights_ascending_queue.append((right_max_idx, curr_height))
            
        n = len(heights)
        while heights_ascending_queue:
            left_min_idx, left_min_height = heights_ascending_queue.popleft()
            max_area = max(max_area, left_min_height * (n - left_min_idx))

        return max_area