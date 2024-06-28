class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        cities_freqs = sorted(Counter(itertools.chain.from_iterable(roads)).values(), reverse=True)
        
        return sum(map(operator.mul, cities_freqs, range(n, 0, -1)))