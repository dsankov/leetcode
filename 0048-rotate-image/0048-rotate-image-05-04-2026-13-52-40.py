class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for s in range(0, n // 2):
            top_row = s
            bottom_row = n - 1 - s
            left_col = s
            right_col = n - 1 - s
            for d in range(n - 2 * s - 1):
                (
                    matrix[top_row][left_col + d],
                    matrix[top_row + d][right_col],
                    matrix[bottom_row][right_col - d],
                    matrix[bottom_row - d][left_col],
                ) = (
                    matrix[bottom_row - d][left_col],
                    matrix[top_row][left_col + d],
                    matrix[top_row + d][right_col],
                    matrix[bottom_row][right_col - d],
                )
