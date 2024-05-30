class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def get_circle(y, x, n, m):
            circle = []
            dy = 0
            for dx in range(m):
                circle.append(matrix[y+dy][x+dx])
            for dy in range(1, n):
                circle.append(matrix[y+dy][x+dx])
            if n > 1:
                for dx in range(m-2,-1,-1):
                    circle.append(matrix[y+dy][x+dx])
            if m > 1:
                for dy in range(n-2, 0, -1):
                    circle.append(matrix[y+dy][x+dx])
            return circle

        n = len(matrix)
        m = len(matrix[0])
        x, y = 0, 0
        result = []
        while n > 0 and m > 0:
            result.extend(get_circle(y, x, n, m))
            y += 1
            x += 1
            n -= 2
            m -= 2
        return result