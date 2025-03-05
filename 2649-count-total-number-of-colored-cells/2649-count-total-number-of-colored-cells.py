class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 0:
            return 0
        iteration = 1
        num_cells = 1
        while iteration < n:
            num_cells += 4 * iteration
            iteration += 1
        return num_cells



        