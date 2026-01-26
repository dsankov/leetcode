class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = inf
        result = []
        for a, b in pairwise(arr):
            if b - a < min_diff:
                min_diff = b - a
                result = [[a, b]]
            elif b - a == min_diff:
                result.append([a, b])
        return result
        