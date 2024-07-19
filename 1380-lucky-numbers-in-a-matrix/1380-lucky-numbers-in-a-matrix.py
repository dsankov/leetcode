class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        mins = [inf] * n
        maxs = [0] * m
        for i in range(n):
            for j in range(m):
                mins[i] = min(mins[i], matrix[i][j])
                maxs[j] = max(maxs[j], matrix[i][j])
        return set(mins) & set(maxs)
        