class Solution:
    class UnionFind():
        def __init__(self, n: int):
            self.parent = list(range(n + 1))
            self.rank = [1] * (n + 1)

        def find(self, node):
            if self.parent[node] == node:
                return node
            self.parent[node] = self.find(self.parent[node])
            return self.parent[node]

        def union(self, x, y):
            root_x, root_y = self.find(x), self.find(y)
            if root_x == root_y:
                return
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x
            self.rank[root_x] += 1
            self.parent[root_y] = root_x

    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        self.n = n
        self.adjacent_list = [set() for _ in range(n + 1)]
        uf = self.UnionFind(n)
        for u, v in edges:
            self.adjacent_list[u].add(v)
            self.adjacent_list[v].add(u)
            uf.union(u, v)

        num_of_groups_for_component = defaultdict(int)
        for node in range(1, n + 1):
            num_of_groups = self.get_num_of_groups(node)
            if num_of_groups == -1:
                return -1
            root_node = uf.find(node)
            num_of_groups_for_component[root_node] = max(
                num_of_groups_for_component[root_node],
                num_of_groups
            )

        return sum(num_of_groups_for_component.values())

    def get_num_of_groups(self, source):
        node_queue = deque([source])
        layer_of_node = [-1] * (self.n + 1)
        layer_of_node[source] = 0
        cur_layer = 0
 
        while node_queue:
            layer_size = len(node_queue)
            for _ in range(layer_size):
                cur_node = node_queue.popleft()
                for neighbor in self.adjacent_list[cur_node]:
                    if layer_of_node[neighbor] == cur_layer:
                        return -1
                    if layer_of_node[neighbor] == -1:
                        layer_of_node[neighbor] = cur_layer + 1
                        node_queue.append(neighbor)
            cur_layer += 1
        return cur_layer

        