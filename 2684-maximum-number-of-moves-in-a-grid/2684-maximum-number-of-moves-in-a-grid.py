class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        DIRECTIONS = ((-1,-1), (0, -1), (1, -1))
        m, n = len(grid), len(grid[0])
        def on_board(y, x):
            return 0 <= y < m

        prev_column = [1] * m
        result = 0
        for col in range(1, n):
            current_column = [0] * m
            for row in range(m):
                curr_max = 0
                for d_y, d_x in DIRECTIONS:
                    test_row, test_col = row + d_y, col + d_x
                    if (
                        on_board(test_row, test_col) 
                        and prev_column[test_row] > 0
                        and grid[test_row][test_col] < grid[row][col]
                    ):
                        curr_max = max(
                            curr_max,
                            1 + prev_column[test_row]
                        )
                        result = max(result, curr_max)

                current_column[row] = curr_max
            prev_column = current_column
        return result - 1 if result > 1 else 0

        