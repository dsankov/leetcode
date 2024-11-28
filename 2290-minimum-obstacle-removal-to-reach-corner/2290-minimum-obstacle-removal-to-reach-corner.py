class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        n, m = len(grid[0]), len(grid)
        min_path_cost = [[inf] * n for _ in range(m)]
        min_path_cost[0][0] = 0
        cells_queue = deque()
        cells_queue.append((0,0))
        while cells_queue:
            row, col = cells_queue.popleft()
            if (row, col) == (m - 1, n - 1):
                return min_path_cost[row][col]
            for d_col, d_row in directions:
                new_row, new_col = row + d_row, col + d_col
                if (0 <= new_row < m and 0 <= new_col < n
                    and min_path_cost[row][col] + grid[new_row][new_col] < min_path_cost[new_row][new_col]
                ):
                        min_path_cost[new_row][new_col] = min_path_cost[row][col] + grid[new_row][new_col]
                        if grid[new_row][new_col] == 0:
                            cells_queue.appendleft((new_row, new_col))
                        else:
                            cells_queue.append((new_row, new_col))

        return -1
            
