class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        UNGUARDED, GUARD, WALL, GUARDED = range(4)
        grid = [[UNGUARDED] * n for _ in range(m)]
        for guard_row, guard_col in guards:
            grid[guard_row][guard_col] = GUARD
        for wall_row, wall_col in walls:
            grid[wall_row][wall_col] = WALL
        
        def mark_direction(line, direction):
            match direction:
                case "L":
                    row = line
                    is_guarded = (grid[row][0] == GUARD)
                    for col in range(n):
                        if is_guarded and grid[row][col] == UNGUARDED:
                            grid[row][col] = GUARDED
                        if grid[row][col] == GUARD:
                            is_guarded = True
                        if grid[row][col] == WALL:
                            is_guarded = False
                case "R":
                    row = line
                    is_guarded = (grid[row][n-1] == GUARD)
                    for col in range(n-1, -1, -1):
                        if is_guarded and grid[row][col] == UNGUARDED:
                            grid[row][col] = GUARDED
                        if grid[row][col] == GUARD:
                            is_guarded = True
                        if grid[row][col] == WALL:
                            is_guarded = False                
                case "D":
                    col = line
                    is_guarded = (grid[0][col] == GUARD)
                    for row in range(m):
                        if is_guarded and grid[row][col] == UNGUARDED:
                            grid[row][col] = GUARDED
                        if grid[row][col] == GUARD:
                            is_guarded = True
                        if grid[row][col] == WALL:
                            is_guarded = False                
                case "U":
                    col = line
                    is_guarded = (grid[m-1][col] == GUARD)
                    for row in range(m-1, -1, -1):
                        if is_guarded and grid[row][col] == UNGUARDED:
                            grid[row][col] = GUARDED
                        if grid[row][col] == GUARD:
                            is_guarded = True
                        if grid[row][col] == WALL:
                            is_guarded = False
            

        for row in range(m):
            for direction in "LR":
                mark_direction(row, direction)
        for col in range(n):
            for direction in "UD":
                mark_direction(col, direction)

        return sum(grid[row][col] == UNGUARDED for row in range(m) for col in range(n))