class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        strongest = set(range(n))
        for srtonger, weaker in edges:
            strongest.discard(weaker)
        return next(iter(strongest)) if len(strongest) == 1 else -1
        