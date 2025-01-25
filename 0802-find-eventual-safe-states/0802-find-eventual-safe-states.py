class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        node_indegrees = [0] * n
        revert_graph = [[] for _ in range(n)]

        for parent, children in enumerate(graph):
            for child in children:
                revert_graph[child].append(parent)
                node_indegrees[parent] += 1

        edge_queue = []
        for node, indegree in enumerate(node_indegrees):
            if indegree == 0:
                edge_queue.append(node)

        safe_nodes = [False] * n
        while edge_queue:
            node = edge_queue.pop()
            safe_nodes[node] = True

            for child in revert_graph[node]:
                node_indegrees[child] -= 1
                if node_indegrees[child] == 0:
                    edge_queue.append(child)

        result = [node for node, is_safe in enumerate(safe_nodes) if is_safe]
        return result        