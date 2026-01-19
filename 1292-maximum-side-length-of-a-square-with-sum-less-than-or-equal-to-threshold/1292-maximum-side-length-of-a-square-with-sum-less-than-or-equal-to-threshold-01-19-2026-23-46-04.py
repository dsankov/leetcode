class Solution:
    def build_prefixsums_matrix(self, mat) -> None:
        self.sums = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        for row in range(self.m):
            for col in range(self.n):
                self.sums[row+1][col+1] = mat[row][col] + self.sums[row][col+1] + self.sums[row+1][col] - self.sums[row][col]

    def get_square_sum(self, bottom_row, right_col, size) -> int:
        return (
                      self.sums[bottom_row ][right_col] 
                    - self.sums[bottom_row - size][right_col] 
                    - self.sums[bottom_row][right_col - size] 
                    + self.sums[bottom_row - size][right_col - size]
                    )
    def is_valid(self,  bottom_row, right_col, size) -> bool:
        return self.get_square_sum(bottom_row, right_col, size) <= self.threshold

    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        self.m = len(mat)
        self.n = len(mat[0])
        self.threshold = threshold

        self.build_prefixsums_matrix(mat)
        # print(self.sums)

        max_size = min(self.m, self.n)
        # print(max_size)
        seen_size = 0

        for bottom_row in range (1, self.m + 1):
            # print("##", seen_size)
            if seen_size >= max_size:
                return seen_size
            if bottom_row <= seen_size:
                continue

            for right_col in range(1, self.n +1):
                if bottom_row <= seen_size:
                    break
                if right_col <= seen_size:
                    continue
                # print(bottom_row, right_col, seen_size)
                if self.is_valid(bottom_row, right_col, seen_size + 1):
                    seen_size += 1 
                    # print("!")

        return seen_size
                


        