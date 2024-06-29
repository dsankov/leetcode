class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adjacents = [[] for _ in range(n)]
        income_edges = [0] * n
        for from_node, to_node in edges:
            adjacents[from_node].append(to_node)
            income_edges[to_node] += 1
        no_ancestors = deque([i for i in range(n) if income_edges[i] == 0])
        topological_order = []
        while no_ancestors:
            node = no_ancestors.popleft()
            topological_order.append(node)
            for neighbor in adjacents[node]:
                income_edges[neighbor] -= 1
                if income_edges[neighbor] == 0:
                    no_ancestors.append(neighbor)
        ancestors_sets = [set() for _ in range(n)]
        for node in topological_order:
            for neighbor in adjacents[node]:
                ancestors_sets[neighbor].add(node)
                ancestors_sets[neighbor] |= ancestors_sets[node]

        return [sorted(list(ancestors_sets[i])) for i in range(n)]
        