class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for (u_vertex, v_vertex), edge_prob in zip(edges, succProb):
            graph[u_vertex].append((v_vertex, edge_prob))
            graph[v_vertex].append((u_vertex, edge_prob))

        max_prob = [0.0] * n
        max_prob[start_node] = 1.0

        probability_queue = deque([start_node])
        while probability_queue:
            current_node = probability_queue.popleft()
            for next_node, path_probability in graph[current_node]:
                new_path_probability = max_prob[current_node] * path_probability
                if new_path_probability > max_prob[next_node]:
                    max_prob[next_node] = new_path_probability
                    probability_queue.append(next_node)

        return max_prob[end_node]