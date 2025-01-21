class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        first_row = sum(grid[0])
        second_row = 0
        min_gain = inf
        for cell_1, cell_2 in zip(grid[0], grid[1]):
            first_row -= cell_1
            best_choice = max(first_row, second_row)
            second_row += cell_2
            min_gain = min(min_gain, best_choice)
        return min_gain
        