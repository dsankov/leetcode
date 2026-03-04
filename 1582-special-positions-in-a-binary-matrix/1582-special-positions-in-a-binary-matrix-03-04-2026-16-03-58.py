class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = [sum(row) for row in mat]
        cols = [sum(col) for col in zip(*mat)]

        single_cell_rows = [i for i, num in enumerate(rows) if num == 1]
        single_cell_cols = [i for i, num in enumerate(cols) if num == 1]

        result = 0
        for row in single_cell_rows:
            for col in single_cell_cols:
                result += mat[row][col]
                # if mat[row][col] == 1:
                #     result += 1
                
        return result
        