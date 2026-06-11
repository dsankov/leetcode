class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        nodes_queue = deque()
        nodes_queue.append(1)
        tree_depth = -1
        visited = set()
        while nodes_queue:
            tree_depth += 1
            level_width = len(nodes_queue)
            for _ in range(level_width):
                u = nodes_queue.popleft()
                visited.add(u)
                for v in graph[u]:
                    if v not in visited:
                        nodes_queue.append(v)
        if tree_depth == 0:
            return 0
        return pow(2, tree_depth - 1, 10**9 + 7)
        

        