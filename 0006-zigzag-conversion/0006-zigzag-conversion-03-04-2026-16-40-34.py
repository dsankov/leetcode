class Solution:
    def convert(self, s: str, numRows: int) -> str:
        def zigzag_move():
            while True:
                for step in range(numRows - 1):
                    yield  1
                for step in range(numRows - 1):
                    yield -1

        move_generator = zigzag_move()

        matrix = [""] * numRows
        row = 0
        for char in s:
            matrix[row] += char
            row += next(move_generator)

        return "".join(matrix)

        