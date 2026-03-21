class Solution:
    def reverseSubmatrix(
        self, grid: List[List[int]], row: int, col: int, k: int
    ) -> List[List[int]]:
        for d_col in range(k):
            for d_row in range(k // 2):
                grid[row + d_row][col + d_col], grid[row + k -1 - d_row][col + d_col] = (
                    grid[row + k-1 - d_row][col + d_col],
                    grid[row + d_row][col + d_col],
                )
        return grid
