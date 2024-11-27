class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adjacency_list = defaultdict(list)
        for vertex in range(0, n - 1):
            adjacency_list[vertex].append(vertex + 1)

        shortest_path = list(range(n))
        result = []
        for u, v in queries:
            adjacency_list[u].append(v)
            if shortest_path[u] >= shortest_path[v]:
                result.append(shortest_path[-1])
                continue
            shortest_path[v] = shortest_path[u] + 1
            vertex_queue = deque([v])
            while vertex_queue:
                curr_vertex = vertex_queue.popleft()
                for curr_neighbor in adjacency_list[curr_vertex]:
                    if shortest_path[curr_neighbor] > shortest_path[curr_vertex] + 1:
                        shortest_path[curr_neighbor] = shortest_path[curr_vertex] + 1
                        vertex_queue.append(curr_neighbor)
            result.append(shortest_path[-1])

        return result
