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

        numbers_stack = [first_number]
        while numbers_stack:
            curr_number = numbers_stack[-1]
            if adjacency_list[curr_number]:
                next_number = adjacency_list[curr_number].pop()
                numbers_stack.append(next_number)
            else:
                path.append(curr_number)
                numbers_stack.pop()

        return [[path[i], path[i-1]] for i in range(len(path)-1, 0, -1)]

    