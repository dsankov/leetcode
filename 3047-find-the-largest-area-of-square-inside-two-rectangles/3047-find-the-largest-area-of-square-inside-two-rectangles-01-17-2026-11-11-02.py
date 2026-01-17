class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)

        max_square_l = 0
        for i in range(n):
            a_x1, a_y1 = bottomLeft[i]
            a_x2, a_y2 = topRight[i]
            for j in range(i+1, n):
                b_x1, b_y1 = bottomLeft[j]
                b_x2, b_y2 = topRight[j]

                if (a_x1 >= b_x2 
                    or a_x2 <= b_x1
                    or a_y1 >= b_y2
                    or a_y2 <= b_y1
                     ):
                        continue
                c_x1, c_y1 = max(a_x1, b_x1), max(a_y1, b_y1)
                c_x2, c_y2 = min(a_x2, b_x2), min(a_y2, b_y2)
                square_l = min(c_x2 - c_x1, c_y2 - c_y1)
                max_square_l = max(max_square_l, square_l)

        return max_square_l **2