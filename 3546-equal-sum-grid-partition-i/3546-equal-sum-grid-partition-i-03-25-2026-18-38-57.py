class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        row_sums = [sum(row) for row in grid]
        col_sums = [sum(col) for col in zip(*grid)]
        total_sum = sum(row_sums)

        row_prefix_sum = row_sums[0] 
        for h_split in range(1, len(grid)):
            if row_prefix_sum == total_sum - row_prefix_sum:
                return True
            row_prefix_sum += row_sums[h_split]
        
        col_prefix_sum = col_sums[0]
        for v_split in range(1, len(grid[0])):
            if col_prefix_sum == total_sum - col_prefix_sum:
                return True
            col_prefix_sum += col_sums[v_split]

        return False

        
        