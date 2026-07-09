class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find_root(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find_root(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        u = self.find_root(u)
        v = self.find_root(v)

        if self.rank[u] < self.rank[v]:
            u, v = v, u
        self.rank[u] += self.rank[v]
        self.parent[v] = u


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        nodes_dsu = DSU(n)
        for i in range(1, n):
            if abs(nums[i-1] - nums[i]) <= maxDiff:
                nodes_dsu.union(i-1, i)

        result = []
        for u, v in queries:
            result.append(nodes_dsu.find_root(u) == nodes_dsu.find_root(v))

        return result


        