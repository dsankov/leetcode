class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        node_indegrees = [0] * n
        revert_graph = [[] for _ in range(n)]

        for i in range(n):
            for node in graph[i]:
                revert_graph[node].append(i)
                node_indegrees[i] += 1

        edge_queue = deque()
        for i in range(n):
            if node_indegrees[i] == 0:
                edge_queue.append(i)

        safe_nodes = [False] * n
        while edge_queue:
            node = edge_queue.popleft()
            safe_nodes[node] = True

            for neighbor in revert_graph[node]:
                node_indegrees[neighbor] -= 1
                if node_indegrees[neighbor] == 0:
                    edge_queue.append(neighbor)

        result = []
        for i in range(n):
            if safe_nodes[i]:
                result.append(i)
        return result        