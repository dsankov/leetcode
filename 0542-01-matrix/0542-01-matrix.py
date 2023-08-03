class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def get_neighbours_top_left(point):
            neighbours = []
            for offset in [[-1, 0], [0, -1] ]:
                if 0 <= point[0] + offset[0] < m and 0 <= point[1] + offset[1] < n:
                    neighbours.append([point[0] + offset[0], point[1] + offset[1]])
            return neighbours
        
        def get_neighbours_bottom_right(point):
            neighbours = []
            for offset in [[1, 0], [0, 1] ]:
                if 0 <= point[0] + offset[0] < m and 0 <= point[1] + offset[1] < n:
                    neighbours.append([point[0] + offset[0], point[1] + offset[1]])
            return neighbours

        m = len(mat)
        n = len(mat[0])
        result = [[float('inf')]*n for _ in range(m)]
        for y in range(m):
            for x in range(n):
                if mat[y][x] == 0:
                    result[y][x] = 0

        for y in range(m):
            for x in range(n):
                neighbours = get_neighbours_top_left([y,x])
                for neighbour in neighbours:
                    result[y][x] = min(
                        result[y][x], 
                        result[neighbour[0]][neighbour[1]] + 1
                        )   

        for y in range(m-1, -1, -1):
            for x in range(n-1, -1, -1):
                neighbours = get_neighbours_bottom_right([y,x])
                for neighbour in neighbours:
                    result[y][x] = min(
                        result[y][x], 
                        result[neighbour[0]][neighbour[1]] + 1
                        )   


            
        return result