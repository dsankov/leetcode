class UnionFind:
    def __init__(self, size: int):
        self.parents = list(range(size))
        self.rank = [1] * size
        self.number_of_components = size
    def find(self, node):
        parent = self.parents[node]
        if node != parent:
            self.parents[node] = self.find(parent)
        return self.parents[node]
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2:
            return False
        bigger_root = root1 if self.rank[root1] >= self.rank[root2] else root2
        smaller_root = root2 if self.rank[root1] >= self.rank[root2] else root1
        self.parents[smaller_root] = bigger_root
        self.rank[bigger_root] += self.rank[smaller_root]
        self.number_of_components -= 1
        return True
    def is_connected(self):
        return self.number_of_components == 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(key=lambda edge: edge[0], reverse=True)
        alice = UnionFind(n)
        bob = UnionFind(n)
        used_edges = 0
        for edge_type, from_edge, to_edge in edges:
            from_edge -= 1
            to_edge -= 1

            if edge_type == 3:
                used_edges += (alice.union(from_edge, to_edge) | bob.union(from_edge, to_edge)) 
            elif edge_type == 2:
                used_edges += bob.union(from_edge, to_edge)
            else:
                used_edges += alice.union(from_edge, to_edge)
        if not(alice.is_connected() and bob.is_connected()):
            return -1
        return len(edges) - used_edges 
        