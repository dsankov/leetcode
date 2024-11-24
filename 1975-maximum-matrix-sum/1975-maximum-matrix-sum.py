class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        flat_matrix = chain.from_iterable(matrix)
        min_abs_value = abs(min(flat_matrix, key=abs))

        flat_matrix = chain.from_iterable(matrix)
        count_negatives = len(list(filter(lambda x: x < 0, flat_matrix)))
        
        flat_matrix = chain.from_iterable(matrix)
        total_sum = sum(abs(x) for x in flat_matrix)
        
        if count_negatives % 2:
            return total_sum - 2 * min_abs_value
        return total_sum
        