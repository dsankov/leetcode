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
        UNSEEN = -1
        n = len(stones)
        uf = self.UnionFind(n)

        seen_row = [UNSEEN] * (10**4 + 1)
        seen_column = [UNSEEN] * (10**4 + 1)
        for curr_index, (curr_col, curr_row) in enumerate(stones):
            if seen_row[curr_row] == UNSEEN:
                seen_row[curr_row] = curr_index
            else:
                uf.union(curr_index, seen_row[curr_row])
            if seen_column[curr_col] == UNSEEN:
                seen_column[curr_col] = curr_index
            else:
                uf.union(curr_index, seen_column[curr_col])

        return n - uf.number_of_components
