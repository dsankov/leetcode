class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        source = [ord(letter) - ord("a") for letter in source]
        target = [ord(letter) - ord("a") for letter in target]
        original = [ord(letter) - ord("a") for letter in original]
        changed = [ord(letter) - ord("a") for letter in changed]

        min_cost = [ [inf] * 26 for _ in range(26) ]
        for source_vertex, dest_vertex, change_cost in zip(original, changed, cost):
            min_cost[source_vertex][dest_vertex] = min(
                min_cost[source_vertex][dest_vertex],
                change_cost
            )
        for intermediate_vertex in range(26):
            for source_vertex in range(26):
                for dest_vertex in range(26):
                    min_cost[source_vertex][dest_vertex] = min(
                        min_cost[source_vertex][dest_vertex],
                        min_cost[source_vertex][intermediate_vertex] + min_cost[intermediate_vertex][dest_vertex]
            )       

        total_cost = 0
        for source_letter, target_letter in zip(source, target):
            if source_letter == target_letter:
                continue
            if min_cost[source_letter][target_letter] == inf:
                return -1
            total_cost += min_cost[source_letter][target_letter]

        return total_cost
