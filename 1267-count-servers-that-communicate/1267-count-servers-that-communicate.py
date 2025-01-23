class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        rows_count = [0] * num_rows
        cols_count = [0] * num_cols
        servers = []
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:
                    servers.append((row, col))
                    rows_count[row] += 1
                    cols_count[col] += 1
        connected_servers = 0
        for row, col in servers:
            if rows_count[row] > 1 or cols_count[col] > 1:
                connected_servers += 1

        return connected_servers

        