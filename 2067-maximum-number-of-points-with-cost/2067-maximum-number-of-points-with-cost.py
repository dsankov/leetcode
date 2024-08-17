class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        previous_row = points[0]
        current_row = previous_row.copy()

        max_from_left = [0] * cols
        max_from_right = [0] * cols

        for row in range(1, rows):
            max_from_left[0] = previous_row[0]
            max_from_right[-1] = previous_row[-1]
            
            for col in range(1, cols):
                max_from_left[col] = max(max_from_left[col - 1] - 1, previous_row[col])
                max_from_right[cols - 1 - col] = max(max_from_right[cols - col] - 1, previous_row[cols - 1 - col])

            for col in range(cols):
                current_row[col] = (
                    points[row][col]
                    + max(max_from_left[col], max_from_right[col])
                )
            previous_row = current_row
        
        return max(previous_row)