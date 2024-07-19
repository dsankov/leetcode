class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mins = {min(row) for row in matrix}
        maxs = {max(column) for column in zip(*matrix)}
        return mins & maxs
        