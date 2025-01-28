class Solution:
    class UnionFind():
        def __init__(self, grid):
            self.parent = defaultdict(tuple)
            self.amount = defaultdict(tuple)
            self.num_rows, self.num_cols = len(grid), len(grid[0])
            
            for cur_row in range(self.num_rows):
                for cur_col in range(self.num_cols):
                    if grid[cur_row][cur_col] == 0:
                        continue
                    self.amount[(cur_row, cur_col)] = grid[cur_row][cur_col]
                    self.parent[(cur_row, cur_col)] = (cur_row, cur_col)
   
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):
            root_x = self.find(x)
            root_y = self.find(y)
            if root_x == root_y:
                return self.amount[root_x]
            
            if self.amount[root_x] > self.amount[root_y]:
                self.parent[root_y] = root_x
                self.amount[root_x] += self.amount[root_y]
                return self.amount[root_x]

            elif self.amount[root_y] > self.amount[root_x]:
                self.parent[root_x] = root_y
                self.amount[root_y] += self.amount[root_x]
                return self.amount[root_y]

            else: # Ranks are equal
                self.parent[root_y] = root_x
                self.amount[root_x] += self.amount[root_y]
                return self.amount[root_x]

    def findMaxFish(self, grid: List[List[int]]) -> int:
        grid_uf = self.UnionFind(grid)
        max_sea_amount = 0
        for cur_row in range(grid_uf.num_rows):
                for cur_col in range(grid_uf.num_cols):
                    if grid[cur_row][cur_col] == 0:
                        continue

                    cur_sea_amount = grid[cur_row][cur_col]
                    for d_row, d_col in ((0, 1), (0, -1),
                                        (1, 0), (-1, 0)
                    ):
                        new_row, new_col = cur_row + d_row, cur_col + d_col
                        if (0 <= new_row < grid_uf.num_rows and 0 <= new_col < grid_uf.num_cols
                            and grid[new_row][new_col] != 0
                            ):
                                cur_sea_amount = grid_uf.union((cur_row, cur_col), (new_row, new_col))
                    max_sea_amount = max(max_sea_amount, cur_sea_amount)

                   
        return max_sea_amount


            


        