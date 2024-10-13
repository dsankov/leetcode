class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        max_num = -inf
        result_start, result_end = 0, inf
        rows_starts = []
        for row in range(k):
            row_start = nums[row][0]
            max_num = max(max_num, row_start)
            heappush(rows_starts, (row_start, row, 0))

        while len(rows_starts) == k:
            cur_start, cur_row, cur_col = heappop(rows_starts)
            if max_num - cur_start < result_end - result_start:
                result_start, result_end = cur_start, max_num
            next_col = cur_col + 1
            if next_col  < len(nums[cur_row]):
                next_start = nums[cur_row][next_col]
                max_num = max(max_num, next_start)
                heappush(rows_starts, (next_start, cur_row, next_col))
        return [result_start, result_end]
        