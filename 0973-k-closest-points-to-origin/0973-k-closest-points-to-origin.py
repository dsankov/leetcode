import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_with_distance = []
        for id, point in enumerate(points):
            points_with_distance.append((point[0]**2 + point[1]**2, point[0], point[1]))

        heapq.heapify(points_with_distance)
        return [[x, y] for _, x, y in  heapq.nsmallest(k, points_with_distance)]