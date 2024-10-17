class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        adjacency_list = [[] for _ in range(n)]
        for start_city, end_city, weight in edges:
            adjacency_list[start_city].append((end_city, weight))
            adjacency_list[end_city].append((start_city, weight))
        min_number_of_reacheble_cities = n
        most_isolated_city = 0
        for city in range(n):
            distances = [inf] * n
            distances[city] = 0
            cities_pq = [(0, city)]
            while cities_pq:
                current_cost, current_city = heappop(cities_pq)
                for neighbor_city, local_cost in adjacency_list[current_city]:
                    new_distance = current_cost + local_cost
                    if new_distance < distances[neighbor_city]:
                        distances[neighbor_city] = new_distance
                        heappush(cities_pq, (new_distance, neighbor_city))
            number_of_reacheble_cities_less_than_threshold = sum(
                1 for test_city in range(n) if test_city != city and distances[test_city] <= distanceThreshold
            )
            if number_of_reacheble_cities_less_than_threshold <= min_number_of_reacheble_cities:
                min_number_of_reacheble_cities = number_of_reacheble_cities_less_than_threshold
                most_isolated_city = city
        return most_isolated_city

    