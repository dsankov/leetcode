class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda balloon: balloon[1])
        last_shot = points[0][1]
        num_arrows = 1
        for balloon_start, balloon_end in points:
            if balloon_start > last_shot:
                num_arrows += 1
                last_shot = balloon_end
        return num_arrows
        