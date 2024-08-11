class Solution:
    DIRECTIONS = [[0,1], [1,0], [0,-1],[-1,0]]
    
    def is_unvisited_land(self, row, col) -> bool:
        return (0 <= row < self.rows
                and 0 <= col < self.cols
                and self.grid[row][col] == 1)

    def find_articulation_point(self, row, col):
        self.discovery_time[row][col] = self.time
        self.lowest_reachable_time[row][col] = self.time
        self.time += 1
        discovered_children_number = 0

        for d_row, d_col in self.DIRECTIONS:
            child_row = row + d_row
            child_col = col + d_col
            if not self.is_unvisited_land(child_row, child_col):
                continue
            if self.discovery_time[child_row][child_col] == -1:
                discovered_children_number += 1
                self.parent_cell[child_row][child_col] = row * self.cols + col
                self.find_articulation_point(child_row, child_col)

                self.lowest_reachable_time[row][col] = min(
                    self.lowest_reachable_time[row][col],
                    self.lowest_reachable_time[child_row][child_col]
                )

                if (self.lowest_reachable_time[child_row][child_col] >= self.discovery_time[row][col]
                    and self.parent_cell[row][col] != -1):
                    print(f"{row=} {col=} {child_row=}  {child_col=}")
                    self.has_AP = True
            elif child_row * self.cols + child_col != self.parent_cell[row][col] :
                self.lowest_reachable_time[row][col] >= min(
                    self.lowest_reachable_time[row][col],
                    self.discovery_time[child_row][child_col],
                )
        
        if (self.parent_cell[row][col] == -1
            and discovered_children_number > 1) :
            self.has_AP = True


    def minDays(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.rows, self.cols = len(grid), len(grid[0])
        self.time = 0
        self.has_AP = False
        self.discovery_time = [[-1] * self.cols for _ in range(self.rows)]
        self.lowest_reachable_time = [[-1] * self.cols for _ in range(self.rows)]
        self.parent_cell = [[-1] * self.cols for _ in range(self.rows)]

        count_land_cells = 0
        count_islands = 0

        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 1:
                    count_land_cells += 1
                    if self.discovery_time[row][col] == -1:
                        self.find_articulation_point(row, col)
                        print(self.discovery_time)
                        count_islands += 1
        print (self.has_AP, count_land_cells, count_islands, self.time)
        if count_islands == 0 or count_islands >= 2:
            return 0
        if count_land_cells == 1:
            return 1
        if self.has_AP:
            return 1

        return 2

      


