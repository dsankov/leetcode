class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda int: (int[0], -int[1]))
        interval_count = len(intervals)
        max_end = 0
        for int_start, int_end in intervals:
            if int_end <= max_end:
                interval_count -= 1
            else:
                max_end = int_end
            
        return interval_count
