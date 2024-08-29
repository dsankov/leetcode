class Solution:
    class UnionFind:
        NO_PARENT = -1
        def __init__(self, n):
            self.parent = [self.NO_PARENT] * n
            self.number_of_components = n

        def find_root(self, node):
            if self.parent[node] == self.NO_PARENT:
                return node
            self.parent[node] = self.find_root(self.parent[node])
            return self.parent[node]

        def union(self, node_1, node_2):
            root_1 = self.find_root(node_1)
            root_2 = self.find_root(node_2)
            if root_1 == root_2:
                return

            self.number_of_components -= 1
            self.parent[root_1] = root_2



    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        uf = self.UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if (stones[i][0] == stones[j][0]
                    or stones[i][1] == stones[j][1]):
                        uf.union(i, j)

        return n - uf.number_of_components
