class Solution:
    WATER = 0
    class UnionFind():
        def __init__(self, grid):
            n = len(grid)
            self.parent = {}
            self.area = {}
            for row in range(n):
                for col in range(n):
                    if grid[row][col] == Solution.WATER:
                        continue
                    self.parent[(row, col)] = (row, col)
                    self.area[(row, col)] = 1

        def find(self, x):
            if self.parent[x] == x:
                return x
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):
            root_x = self.find(x)
            root_y = self.find(y)
            if root_x == root_y:
                return
            if self.area[root_x] < self.area[root_y]:
                root_x, root_y = root_y, root_x

            self.area[root_x] += self.area[root_y]
            self.parent[root_y] = root_x

    def largestIsland(self, grid: List[List[int]]) -> int:
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        n = len(grid)
        total_land = sum(chain.from_iterable(grid))
        if total_land == n ** 2:
            return total_land

        uf = self.UnionFind(grid)
        for row in range(n):
            for col in range(n):
                if grid[row][col] == self.WATER:
                    continue
                for d_row, d_col in DIRECTIONS:
                    new_row, new_col = row + d_row, col + d_col
                    if not (0 <= new_row < n and 0 <= new_col < n):
                        continue
                    if grid[new_row][new_col] == self.WATER:
                        continue
                    uf.union((row, col), (new_row, new_col))
        
        max_area = 0
        for row in range(n):
            for col in range(n):
                if grid[row][col] != self.WATER:
                    continue
                neighbor_islands = set()
                cur_area = 1
                for d_row, d_col in DIRECTIONS:
                    new_row, new_col = row + d_row, col + d_col
                    if not (0 <= new_row < n and 0 <= new_col < n):
                        continue
                    if grid[new_row][new_col] == self.WATER:
                        continue
                    root_neighbor = uf.find((new_row, new_col))
                    if root_neighbor in neighbor_islands:
                        continue
                    neighbor_islands.add(root_neighbor)
                    cur_area += uf.area[root_neighbor]

                max_area = max(max_area, cur_area)
        
        return max_area
