class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_abs_value = inf
        count_negatives = 0
        total_sum = 0
        for row in matrix:
            for num in row:
                min_abs_value = min(min_abs_value, abs(num))
                total_sum += abs(num)
                if num < 0:
                    count_negatives ^= 1
        if count_negatives:
            return total_sum - 2 * min_abs_value
        return total_sum
        