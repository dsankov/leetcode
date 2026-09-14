class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        r1_x1, r1_y1, r1_x2, r1_y2 = rec1
        r2_x1, r2_y1, r2_x2, r2_y2 = rec2

        x_overlap = (
            r1_x1 < r2_x1 < r1_x2
            or r1_x1 < r2_x2 < r1_x2
            or r2_x1 < r1_x1 < r2_x2
            or r2_x1 < r1_x2 < r2_x2
            or r1_x1 == r2_x1 and r1_x2 == r2_x2
        )
        y_overlap = (
            r1_y1 < r2_y1 < r1_y2
            or r1_y1 < r2_y2 < r1_y2
            or r2_y1 < r1_y1 < r2_y2
            or r2_y1 < r1_y2 < r2_y2
            or r1_y1 == r2_y1 and r1_y2 == r2_y2
        )
        return x_overlap and y_overlap
