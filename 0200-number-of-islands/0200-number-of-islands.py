class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        WATER, LAND, VISITED = map(str, range(3))
        ADJACENTS = [[0,1], [1,0], [0,-1], [-1,0]]
        n = len(grid)
        m = len(grid[0])
        num_islands = 0

        def flood_fill(row, col):
            cells_stack = [(row,col)]
            while cells_stack:
                row, col = cells_stack.pop()
                grid[row][col] = VISITED
                for d_row, d_col in ADJACENTS:
                    if (0 <= row+d_row < n and 0 <= col+d_col < m
                        and grid[row+d_row][col+d_col] == LAND):
                            cells_stack.append((row + d_row, col + d_col))

        for row in range(n):
            for col in range(m):
                if grid[row][col] == LAND:
                    num_islands += 1
                    flood_fill(row, col)
        return num_islands

        