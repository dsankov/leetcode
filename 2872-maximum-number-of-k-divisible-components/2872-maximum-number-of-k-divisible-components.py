class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n == 1:
            return 1

        adjacency_list = defaultdict(set)
        for u, v in edges:
            adjacency_list[u].add(v)
            adjacency_list[v].add(u)

        leaves_queue = deque(node for node, neighbors in adjacency_list.items() if len(neighbors) == 1)
        components_number = 0
        while leaves_queue:
            curr_leaf = leaves_queue.popleft()
            leaf_neighbor = next(iter(adjacency_list[curr_leaf])) if adjacency_list[curr_leaf] else None
            
            if leaf_neighbor is not None:
                adjacency_list[leaf_neighbor].remove(curr_leaf)
                if len(adjacency_list[leaf_neighbor]) == 1:
                    leaves_queue.append(leaf_neighbor)
           
            if values[curr_leaf] % k == 0:
                components_number += 1
            else:
                values[leaf_neighbor] += values[curr_leaf]
            

        return components_number