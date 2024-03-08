class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY = 0
        FRESH = 1
        ROTTEN =2
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
        n, m = len(grid), len(grid[0])
        
        def get_fresh_neighbours(position: Tuple[int]) -> List[Tuple[int]]:
            y, x = position
            result = []
            for d_y, d_x in directions:
                if 0 <= y + d_y < n \
                and 0 <= x + d_x < m \
                and grid[y + d_y][x + d_x] == FRESH:
                    result.append((y + d_y, x + d_x))
            return result
        
        rotten_oranges_to_proceed = deque()
        fresh_oranges = set()
        minute = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == FRESH:
                    fresh_oranges.add((i,j))
                elif grid[i][j] == ROTTEN:
                    rotten_oranges_to_proceed.append(((i, j), minute)) # (position, minute)
        if not fresh_oranges:
                return minute  # minute == 0          

        visited_oranges = set()
        final_minute = 0
        while rotten_oranges_to_proceed:
            rotten_orange, minute = rotten_oranges_to_proceed.popleft()
            
            if not fresh_oranges:
                return final_minute
            
            fresh_neighbours = get_fresh_neighbours(rotten_orange)
            for fresh_orange in fresh_neighbours:
                if fresh_orange not in visited_oranges:
                    fresh_oranges.remove(fresh_orange)
                    visited_oranges.add(fresh_orange)
                    rotten_oranges_to_proceed.append((fresh_orange, minute + 1))
                    final_minute = max(final_minute, minute + 1)
                    
            
        
        return -1