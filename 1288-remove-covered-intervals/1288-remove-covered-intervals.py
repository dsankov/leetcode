class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda int: (int[0], -int[1]))
        interval_count = n
        for i in range(n):
            a, b = intervals[i]
            for j in range(i):
                x, y = intervals[j]
                print("\t", x, y)
                if x <=a and b <= y:
                    interval_count -= 1
                    break
        return interval_count
