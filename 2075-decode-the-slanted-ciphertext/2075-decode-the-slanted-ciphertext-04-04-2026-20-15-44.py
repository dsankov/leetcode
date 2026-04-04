class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows

        def slanted_gen(rows, cols) -> int:
            shift = rows + 1

            for first_line_start in range(cols + 2 - rows):
                for idx in range(first_line_start, rows * cols, cols + 1):
                    yield idx

        result = []
        slanted = slanted_gen(rows, cols)
        for idx in slanted:
            result.append(encodedText[idx])

        return "".join(result).rstrip()
        