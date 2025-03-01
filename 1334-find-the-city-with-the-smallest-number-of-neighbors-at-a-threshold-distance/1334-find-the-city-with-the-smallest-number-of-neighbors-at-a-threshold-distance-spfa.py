class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        # Adjacency list to store the graph
        adjacency_list = [[] for _ in range(n)]

        # Matrix to store shortest path distances from each city
        shortest_path_matrix = [[float("inf")] * n for _ in range(n)]

        # Initialize adjacency list and shortest path matrix
        for i in range(n):
            shortest_path_matrix[i][i] = 0  # Distance to itself is zero

        # Populate the adjacency list with edges
        for start, end, weight in edges:
            adjacency_list[start].append((end, weight))
            adjacency_list[end].append((start, weight))  # For undirected graph

        # Compute shortest paths from each city using Dijkstra's algorithm
        for i in range(n):
            self.spfa(n, adjacency_list, shortest_path_matrix[i], i)

        # Find the city with the fewest number of reachable cities within the distance threshold
        return self.get_city_with_fewest_reachable(
            n, shortest_path_matrix, distanceThreshold
        )

    # Dijkstra's algorithm to find shortest paths from a source city
    def spfa(
        self,
        n: int,
        adjacency_list: List[List[tuple]],
        shortest_path_distances: List[int],
        source: int,
    ):
        city_queue = deque([source])
        update_count = [0] * n
        shortest_path_distances[:] = [float("inf")] * n
        shortest_path_distances[source] = 0  # Distance to itself is zero

        while city_queue:
            current_city = city_queue.popleft()
            # Update distances to neighboring cities
            for neighbor_city, edge_weight in adjacency_list[current_city]:
                if (
                    shortest_path_distances[neighbor_city]
                    > shortest_path_distances[current_city] + edge_weight
                ):
                    shortest_path_distances[neighbor_city] = shortest_path_distances[current_city] + edge_weight
                    city_queue.append(neighbor_city)
                    update_count[neighbor_city] += 1
                    if update_count[neighbor_city] > n:
                        print("Negative cycle detected")

    # Determine the city with the fewest number of reachable cities within the distance threshold
    def get_city_with_fewest_reachable(
        self,
        n: int,
        shortest_path_matrix: List[List[int]],
        distance_threshold: int,
    ) -> int:
        city_with_fewest_reachable = -1
        fewest_reachable_count = n

        # Count number of cities reachable within the distance threshold for each city
        for i in range(n):
            reachable_count = sum(
                1
                for j in range(n)
                if i != j and shortest_path_matrix[i][j] <= distance_threshold
            )

            # Update the city with the fewest reachable cities
            if reachable_count <= fewest_reachable_count:
                fewest_reachable_count = reachable_count
                city_with_fewest_reachable = i
        return city_with_fewest_reachable        