class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        distance_matrix = [[inf]* n for _ in range(n)]
        for city in range(n):
            distance_matrix[city][city] = 0
        for start_city, end_city, weight in edges:
            distance_matrix[start_city][end_city] = weight
            distance_matrix[end_city][start_city] = weight

        self.floyd_warshall(distance_matrix)

        # Find the city with the fewest number of reachable cities within the distance threshold
        return self.get_city_with_fewest_reachable(
            n, distance_matrix, distanceThreshold
        )

    def floyd_warshall(
        self,
        distance_matrix: List[List[int]]
    ):
        n = len(distance_matrix)
        for intermediate_city in range(n):
            for start_city in range(n):
                for end_city in range(n):
                    distance_matrix[start_city][end_city] = min(
                        distance_matrix[start_city][end_city],
                        distance_matrix[start_city][intermediate_city] + distance_matrix[intermediate_city][end_city]
                    )
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