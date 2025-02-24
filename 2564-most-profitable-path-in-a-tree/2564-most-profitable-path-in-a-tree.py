class Solution:
    def __init__(self):
        self.adjacent_list = defaultdict(list)
        self.visited = set()
        self.max_income = float("-inf")
        self.bob_path = {}
        # self.max_income

    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        self.n = len(amount)
        self.amount = amount
        for u, v in edges:
            self.adjacent_list[u].append(v)
            self.adjacent_list[v].append(u)
    
        self.find_bob_path(bob, 0)

        self.visited = set()
        self.find_alice_path(0, 0, 0)

        return self.max_income

    def find_bob_path(self, source_node, cur_time):
        self.bob_path[source_node] = cur_time
        self.visited.add(source_node)

        if source_node == 0:
            return True

        for adjacent_node in self.adjacent_list[source_node]:
            if (adjacent_node not in self.visited
                and self.find_bob_path(adjacent_node, cur_time + 1)
                ):
                    return True

        self.bob_path.pop(source_node, None)
        return False

    def find_alice_path(self, source_node, cur_time, cur_income):
        self.visited.add(source_node)
        if (
            source_node not in self.bob_path
            or cur_time < self.bob_path[source_node]
        ):
            cur_income += self.amount[source_node]

        elif cur_time == self.bob_path[source_node]:
            cur_income += self.amount[source_node] // 2

        if (
            source_node != 0 
            and len(self.adjacent_list[source_node]) == 1
        ):
                self.max_income = max(self.max_income, cur_income)

        for adjacent_node in self.adjacent_list[source_node]:
            if adjacent_node not in self.visited:
                self.find_alice_path(adjacent_node, cur_time + 1, cur_income) 



        