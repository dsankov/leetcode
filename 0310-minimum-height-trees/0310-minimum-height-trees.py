from pprint import pp
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))

        adjacency_list = defaultdict(list)
        in_degree = [0] * n
        for a, b in edges:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)
            in_degree[a] += 1
            in_degree[b] += 1
        
        leaves_queue = deque()
        not_leaves = set()
        for node in range(n):
            if in_degree[node] == 1:
                leaves_queue.append(node)
            else:
                not_leaves.add(node)

        while leaves_queue:
            if len(not_leaves) <= 2:
                return list(not_leaves)

            queue_size = len(leaves_queue)
            for _ in range(queue_size):
                curr_node = leaves_queue.popleft()
                not_leaves.discard(curr_node)

                for neighbor in adjacency_list[curr_node]:
                    if neighbor in not_leaves:
                        in_degree[neighbor] -= 1
                        if in_degree[neighbor] == 1:
                            leaves_queue.append(neighbor)


        
        return None

        