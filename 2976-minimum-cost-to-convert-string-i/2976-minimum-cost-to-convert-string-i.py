class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
    
        # Floyd-Warshall Algorithm

        min_cost_matrix = defaultdict(lambda: inf)
        for source_vertex, dest_vertex, change_cost in zip(original, changed, cost):
            min_cost_matrix[source_vertex, dest_vertex] = min(
                min_cost_matrix[source_vertex, dest_vertex],
                change_cost
            )
        used_letters = list(set(original + changed))
        for intermediate_vertex in used_letters:
            min_cost_matrix[intermediate_vertex, intermediate_vertex] = 0
            for source_vertex in used_letters:
                for dest_vertex in used_letters:
                    min_cost_matrix[source_vertex, dest_vertex] = min(
                        min_cost_matrix[source_vertex, dest_vertex],
                        min_cost_matrix[source_vertex, intermediate_vertex] + min_cost_matrix[intermediate_vertex, dest_vertex]
            )       

        total_cost = 0
        for source_letter, target_letter in zip(source, target):
            if min_cost_matrix[source_letter, target_letter] == inf:
                return -1
            total_cost += min_cost_matrix[source_letter, target_letter]

        return total_cost
