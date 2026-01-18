class Solution:
    def compute_prefix_sums(self):
        self.rows_sums = [[0] * self.n for _ in range(self.m)]
        self.cols_sums = [[0] * self.n for _ in range(self.m)]
        for row in range(self.m):
            self.rows_sums[row][0] = self.grid[row][0]
            for col in range(1, self.n):
                self.rows_sums[row][col] = self.rows_sums[row][col - 1] + self.grid[row][col]
        for col in range(self.n):
            self.cols_sums[0][col] = self.grid[0][col]
            for row in range(1, self.m):
                self.cols_sums[row][col] = self.cols_sums[row - 1][col] + self.grid[row][col]

    def is_magic(self, start_row, start_col, size):
        target_sum = self.rows_sums[start_row][start_col + size - 1] - (self.rows_sums[start_row][start_col - 1] if start_col > 0 else 0)

        

        diag1_sum = 0
        diag2_sum = 0
        for d in range(size):
            diag1_sum += self.grid[start_row + d][start_col + d]
            diag2_sum += self.grid[start_row + size - d - 1][start_col + d]
        if diag1_sum != target_sum or diag2_sum != target_sum:
            return False


        for row in range(start_row + 1, start_row + size):
            if self.rows_sums[row][start_col + size - 1] - (self.rows_sums[row][start_col - 1] if start_col > 0 else 0) != target_sum:
                return False
        for col in range(start_col, start_col + size):
            if self.cols_sums[start_row + size - 1][col] - (self.cols_sums[start_row - 1][col] if start_row > 0 else 0) != target_sum:
                return False

        return True
        

    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        self.max_size = min(self.n, self.m)
        self.grid = grid

        self.compute_prefix_sums()

        for size in range(self.max_size, 1, -1):
            print(size)
            for row in range(self.m - size + 1):
                for col in range(self.n - size + 1):
                    if self.is_magic(row, col, size):
                        return size
        return 1
        