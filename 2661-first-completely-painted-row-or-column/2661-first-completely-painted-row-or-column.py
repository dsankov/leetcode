class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        num_rows, num_cols = len(mat), len(mat[0])
        num_cells = num_rows * num_cols
        row_count = [0] * num_rows
        col_count = [0] * num_cols
        num_yx = [[-1,-1] for _ in range(num_cells + 1)]
        for row in range(num_rows):
            for col in range(num_cols):
                value = mat[row][col]
                num_yx[value] = [row, col]

        for i in range(num_cells):
            value = arr[i]
            row, col = num_yx[value]
            row_count[row] += 1
            col_count[col] += 1
            if row_count[row] == num_cols or col_count[col] == num_rows:
                return i

        return -1

        