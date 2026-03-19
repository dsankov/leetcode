class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        def accumulate(res, item, sign):
            res["X"] += sign * item["X"]
            res["Y"] += sign * item["Y"]
            res["."] += sign * item["."]

        m, n = len(grid), len(grid[0])
        prev_line = [{"X": 0, "Y": 0, ".": 0} for _ in range(n)]
        result = 0

        for row in range(m):
            cur_line = [{"X": 0, "Y": 0, ".": 0} for _ in range(n)]
            for col in range(n):
                cur_char = grid[row][col]
                cur_line[col][cur_char] += 1
                if row > 0:
                    accumulate(cur_line[col], prev_line[col], 1)
                if col > 0:
                    accumulate(cur_line[col], cur_line[col - 1], 1)
                if row > 0 and col > 0:
                    accumulate(cur_line[col], prev_line[col - 1], -1)

                if cur_line[col]["X"] > 0 and cur_line[col]["X"] == cur_line[col]["Y"]:
                    result += 1
            prev_line = cur_line
            

        return result