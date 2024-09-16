class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minute_points = []
        for time_point in timePoints:
            hh, mm = map(int, time_point.split(":"))
            minute_points.append(mm + hh * 60)
        minute_points.sort()
        min_difference = (24 * 60 - minute_points[-1]) + minute_points[0]
        for point_1, point_2 in zip(minute_points, minute_points[1:]):
            cur_difference = point_2 - point_1
            min_difference = min(min_difference, cur_difference)
        return min_difference
        