class DSU:
    def __init__(self, m , n):
        self.parent = list(range(m * n))
        self.rank = [1] * (m * n)

    def root_of(self, a):
        if a != self.parent[a]:
            self.parent[a] = self.root_of(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        a = self.root_of(a)
        b = self.root_of(b)
        if a == b:
            return False
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.parent[b] = a
        self.rank[a] += 1
        return True

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        left_compliment = {
            1: [1, 4, 6],
            2: [],
            3: [1, 4, 6],
            4: [],
            5: [1, 4, 6],
            6: [],
        }
        top_compliment = {
            1: [],
            2: [2, 3, 4],
            3: [],
            4: [],
            5: [2, 3, 4],
            6: [2, 3, 4],
        }

        m, n = len(grid), len(grid[0])
        street_dsu = DSU(m, n)

        for r in range(m):
            for c in range(n):
                lin_coord = r * n + c
                if r > 0 and grid[r-1][c] in top_compliment[grid[r][c]]:
                    top_coord = (r-1) * n + c
                    street_dsu.union(lin_coord, top_coord)
                if c > 0 and grid[r][c-1] in left_compliment[grid[r][c]]:
                    left_coord = r * n + c - 1
                    street_dsu.union(lin_coord, left_coord)

        start_coord = 0
        finish_coord = (m - 1) * n + (n - 1)
        return street_dsu.root_of(start_coord) == street_dsu.root_of(finish_coord)



        