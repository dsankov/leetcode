class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj_matrix = defaultdict(list)
        for u, v, weight in edges:
            adj_matrix[u].append((v, weight))
            adj_matrix[v].append((u, 2 * weight))

        node_queue = [(0, 0)]
        visited = [False] * n
        cost = 0

        while node_queue:
            cur_cost, node = heappop(node_queue)
            if node == n - 1:
                return cur_cost
            if visited[node]:
                continue
            
            visited[node] = True
            for v, weight in adj_matrix[node]:
                heappush(node_queue, (cur_cost + weight, v))

        return -1

        