from pprint import pp
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adjacency_list = defaultdict(list)
        used_numbers = defaultdict(int)
        for pair_start, pair_end in pairs:
            adjacency_list[pair_start].append(pair_end)
            used_numbers[pair_start] += 1
            used_numbers[pair_end] -= 1

        first_number = -1
        for number, count in used_numbers.items():
            if count == 1:
                first_number = number
                break
        if first_number == -1:
            first_number = next(iter(used_numbers))
        path = []

        def dfs(number):
            while adjacency_list[number]:
                next_number = adjacency_list[number].pop()
                dfs(next_number)
            path.append(number)

        dfs(first_number)
        return [[path[i], path[i-1]] for i in range(len(path)-1, 0, -1)]

    