class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        end = -inf
        result = 0
        for interval_start, interval_end in intervals:
            if interval_start >= end:
                end = interval_end
            else:
                result += 1
        return result
        