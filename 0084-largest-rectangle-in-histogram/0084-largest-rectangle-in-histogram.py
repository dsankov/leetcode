class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights_ascending_queue = deque() # idx, height
        max_area = 0
        for curr_idx, curr_height in enumerate(heights):
            right_max_idx = curr_idx
            curr_max_area = 0
            while heights_ascending_queue:
                if heights_ascending_queue[-1][1] < curr_height:
                    break
                prev_max_idx, prev_max_height = heights_ascending_queue.pop()
                curr_max_area = max(curr_max_area, prev_max_height * (curr_idx - prev_max_idx))
                right_max_idx = prev_max_idx

            curr_max_area = max(curr_max_area, curr_height * (curr_idx - right_max_idx + 1))

            heights_ascending_queue.append((right_max_idx, curr_height))
            max_area = max(max_area, curr_max_area)
        
        n = len(heights)
        while heights_ascending_queue:
            left_min_idx, left_min_height = heights_ascending_queue.popleft()
            max_area = max(max_area, left_min_height * (n - left_min_idx))

        return max_area