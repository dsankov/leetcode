class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for edge_index, (u_vertex, v_vertex) in enumerate(edges):
            graph[u_vertex].append((v_vertex, succProb[edge_index]))
            graph[v_vertex].append((u_vertex, succProb[edge_index]))

        max_prob = [0.0] * n
        max_prob[start_node] = 1.0

        probability_queue = [(-1 * 1.0, start_node)]
        while probability_queue:
            current_probability, current_node = heapq.heappop(probability_queue)
            if current_node == end_node:
                return -current_probability
            for next_node, path_probability in graph[current_node]:
                new_path_probability = (-current_probability * path_probability)
                if new_path_probability > max_prob[next_node]:
                    max_prob[next_node] = new_path_probability
                    heapq.heappush(probability_queue, (-1 * new_path_probability, next_node))

        return 0.0