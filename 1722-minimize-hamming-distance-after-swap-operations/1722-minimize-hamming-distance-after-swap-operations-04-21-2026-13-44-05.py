class DSU:
    def __init__(self, n):
        self.roots = list(range(n))
        self.ranks = [1] * n
        self.group_of = {idx: {idx} for idx in range(n)}

    def root_of(self, idx):
        if self.roots[idx] == idx:
            return idx
        root = self.root_of(self.roots[idx])
        self.roots[idx] = root
        return root

    def union(self, a, b):
        root_a = self.root_of(a)
        root_b = self.root_of(b)
        if root_a == root_b:
            return
        if self.ranks[root_a] >= self.ranks[root_b]:
            self.ranks[root_a] += self.ranks[root_b]
            self.roots[root_b] = root_a
            self.group_of[root_a] |= self.group_of[root_b]
        else:
            self.ranks[root_b] += self.ranks[root_a]
            self.roots[root_a] = root_b
            self.group_of[root_b] |= self.group_of[root_a]

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        groups = DSU(n)

        for a, b in allowedSwaps:
                groups.union(a, b)

        distance = 0
        for idx in range(n):
            if groups.roots[idx] != idx:
                continue

            cur_group = groups.group_of[idx] 
            source_cnt = Counter(source[swap] for swap in cur_group)
            target_cnt = Counter(target[swap] for swap in cur_group)
            for val, count in target_cnt.items():
                distance += max(0, count - source_cnt[val])

        return distance

