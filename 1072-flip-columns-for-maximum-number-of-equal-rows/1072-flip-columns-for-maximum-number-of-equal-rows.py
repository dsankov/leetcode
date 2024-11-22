class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        return max(Counter(tuple(row[0] ^ value for value in row) for row in matrix).values())
        