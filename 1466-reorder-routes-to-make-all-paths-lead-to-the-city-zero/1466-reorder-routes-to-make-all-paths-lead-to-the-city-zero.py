class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        def bfs(node: int, n: int, roads) -> int:
            city_queue = deque()
            city_queue.append(node)
            visited_cities = set()
            visited_cities.add(node)

            count_swap = 0
            while city_queue:
                node = city_queue.popleft()
                for neighbour, direction in roads[node]:
                    if not neighbour in visited_cities:
                        if direction:
                            count_swap += 1
                        visited_cities.add(neighbour)
                        city_queue.append(neighbour)

            return count_swap

        roads = [[] for _ in range(n)]
        for from_city, to_city in connections:
            roads[from_city].append((to_city, True))
            roads[to_city].append((from_city, False))

        result = bfs(0, n, roads)
        return result
