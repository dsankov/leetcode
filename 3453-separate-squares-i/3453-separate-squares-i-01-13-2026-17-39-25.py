class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        total_area = 0
        for x, y, l in squares:
            events.append((y, l))
            events.append((y + l, -l))
            total_area += l * l

        events.sort()
        target_area = total_area / 2.0

        prev_y = events[0][0]
        x_base = 0
        processed_area = 0
        
        for curr_y, x_delta in events:
            y_step = curr_y - prev_y
            if y_step > 0:
                step_area = x_base * y_step
                if processed_area + step_area >= target_area:
                    return prev_y + (target_area - processed_area) / x_base

                processed_area += step_area
            x_base += x_delta
            prev_y = curr_y