class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adjacent_list = [set() for _ in range(n + 1)]
        for u, v in edges:
            adjacent_list[u].add(v)
            adjacent_list[v].add(u)
        leaf_queue = []
        for v in range(1, n + 1):
            if len(adjacent_list[v]) == 1:
                leaf_queue.append(v)

        while leaf_queue:
            u = leaf_queue.pop()
            v = next(iter(adjacent_list[u]))
            adjacent_list[u].remove(v)
            adjacent_list[v].remove(u)
            if len(adjacent_list[v]) == 1:
                leaf_queue.append(v)

        for u, v in reversed(edges):
            if v in adjacent_list[u] and u in adjacent_list[v]:
                return [u, v]

        return [0, 0]
            

