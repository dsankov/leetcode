class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        diameter_1 = self.get_diameter(edges1)
        diameter_2 = self.get_diameter(edges2)
        return max(
                diameter_1,
                diameter_2,
                ceil(diameter_1 / 2) + ceil(diameter_2 / 2) + 1
        )

    def get_diameter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        nodes_degree = [0] * n
        visited_nodes = [False] * n
        leaves_queue = deque()
        adjacency_list = self.get_adjacency_list(edges)

        for node in range(n):
            nodes_degree[node] = len(adjacency_list[node])
            if nodes_degree[node] == 1:
                leaves_queue.append(node)
                visited_nodes[node] = True

        remaining_nodes = n
        removed_layers = 0
        while remaining_nodes > 2:
            for _ in range(len(leaves_queue)):
                curr_leaf = leaves_queue.popleft()
                remaining_nodes -= 1
                for neighbor in adjacency_list[curr_leaf]:
                    if visited_nodes[neighbor]:
                        continue
                    nodes_degree[neighbor] -= 1
                    if nodes_degree[neighbor] == 1:
                        leaves_queue.append(neighbor)
                        visited_nodes[neighbor] = True
            removed_layers += 1

        extra_edge = remaining_nodes - 1
        return removed_layers * 2 + extra_edge



    def get_adjacency_list(self, edges: List[List[int]]) -> List[List[int]]:
        adjacency_list = [[] for _ in range(len(edges) + 1)]
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
        return adjacency_list