class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        UNVISITED = -1
        DIRECTIONS = ((0, 1), (0, -1), (-1, 0), (1, 0))
        num_rows, num_cols = len(isWater), len(isWater[0])
        cells_height = [[UNVISITED] * num_cols for _ in range(num_rows)]
        cells_queue = deque()
        cur_level = 0
        for row in range(num_rows):
            for col in range(num_cols):
                if isWater[row][col] == 1:
                    cells_height[row][col] = cur_level
                    cells_queue.append((row, col))
        next_level = cur_level + 1
        while cells_queue:
            level_size = len(cells_queue)
            for _ in range(level_size):
                cur_row, cur_col = cells_queue.popleft()
                for d_row, d_col in DIRECTIONS:
                    new_row, new_col = cur_row + d_row, cur_col + d_col
                    if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                        if cells_height[new_row][new_col] == UNVISITED:
                            cells_height[new_row][new_col] = next_level
                            cells_queue.append((new_row, new_col))
            next_level += 1
        return cells_height
        