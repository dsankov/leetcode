class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        def dfs(y, x):
            # If out of bounds or it's water in grid2, return True (base case)
            if (
                y < 0 or y >= m 
                or x < 0 or x >= n 
                or grid2[y][x] == 0
            ):
                return True
            # Mark this cell as visited by setting it to 0
            grid2[y][x] = 0
            # Check if this cell is part of a valid sub-island
            is_sub_island = (grid1[y][x] == 1)
            # Explore all four directions (up, down, left, right)
            for d_y, d_x in DIRECTIONS:
                is_sub_island &= dfs(y + d_y, x + d_x)
            return is_sub_island
        
        m, n = len(grid1), len(grid2[0])
        sub_island_count = 0
        
        for y in range(m):
            for x in range(n):
                if grid2[y][x] == 1:  # Start a DFS if we find an unvisited island in grid2
                    sub_island_count += int(dfs(y,x))   

        return sub_island_count