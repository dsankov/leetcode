from itertools import pairwise
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        for [source_x, source_y], [target_x, target_y] in pairwise(points):
            result += max(
                abs(source_x - target_x),
                abs(source_y - target_y)
            )

        return result