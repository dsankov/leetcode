class DSU:
    def __init__(self, n: int):
        self.n = n
        self.parent = list(range(n))
        self.rank = [1] * n
        self.num_components = n

    def find(self, u: int):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v) -> bool:
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return False

        self.num_components -= 1
        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
            self.rank[root_u] += self.rank[root_v]
        else:
            self.parent[root_u] = root_v
            self.rank[root_v] += self.rank[root_u]
        return True

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        graph = DSU(n)
        flex_edges = []
        min_strength = inf
        for u, v, s, m in edges:
            if m == 1:
                if not graph.union(u, v):
                    return -1
                min_strength = min(min_strength, s)
            else:
                flex_edges.append((s, u, v))
        if graph.num_components == 1:
            return min_strength

        flex_edges.sort()
        used_edges = []
        while flex_edges:
            s, u, v = flex_edges.pop()
            if not graph.union(u, v):
                continue
            used_edges.append(s)
            if graph.num_components == 1:
                break
        else:
            return -1


        if k == 0:
            return min(min_strength,
                            used_edges[-1]
                         )
        if k >= len(used_edges):
            return min(min_strength,
                            used_edges[-1] * 2
                         )
        return min(min_strength,
                            used_edges[-1] * 2,
                            used_edges[-(k+1)]
                         )
            



        


        