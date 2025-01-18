class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        DIRECTIONS = {
                    1: (0, 1), 
                    2: (0, -1),
                    3: (1, 0),
                    4: (-1, 0)
        }
        num_rows, num_cols = len(grid), len(grid[0])
        start_row, start_col = 0, 0
        target_row, target_col = num_rows - 1, num_cols - 1

        min_cost = [[inf] * num_cols for _ in range(num_rows)]
        min_cost[start_row][start_col] = 0
        cell_deque = deque()
        cell_deque.append((start_row, start_col))

        while cell_deque:
            curr_row, curr_col = cell_deque.popleft()
            if (curr_row, curr_col) == (target_row, target_col):
                return min_cost[target_row][target_col]
            for dir_idx, (d_row, d_col) in DIRECTIONS.items():
                new_row, new_col = curr_row + d_row, curr_col + d_col
                if not (0 <= new_row < num_rows and 0 <= new_col < num_cols):
                    continue
                last_step_cost = 0 if dir_idx == grid[curr_row][curr_col] else 1
                if min_cost[new_row][new_col] <= min_cost[curr_row][curr_col] + last_step_cost:
                    continue
                min_cost[new_row][new_col] = min_cost[curr_row][curr_col] + last_step_cost
                if last_step_cost == 0:
                    cell_deque.appendleft((new_row, new_col))
                else:
                    cell_deque.append((new_row, new_col))

        return min_cost[target_row][target_col] # newer reachable
                    