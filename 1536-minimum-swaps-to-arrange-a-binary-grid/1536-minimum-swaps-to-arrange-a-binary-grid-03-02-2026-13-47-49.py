class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        tail_zeroes = []
        for row in grid:
            zero_count = 0
            for char in reversed(row):
                if char == 0:
                    zero_count += 1
                else:
                    break
            tail_zeroes.append(zero_count)

        moves = 0
        for target_row in range(n):
            for test_row in range(target_row, n):
                if tail_zeroes[test_row] < n - 1- target_row:
                    continue

                moves += (test_row - target_row)
                found_value = tail_zeroes[test_row]
                while test_row > target_row:
                    tail_zeroes[test_row] = tail_zeroes[test_row - 1]
                    test_row -= 1
                tail_zeroes[target_row] = found_value
                break 
            else:
                    return -1

        return moves