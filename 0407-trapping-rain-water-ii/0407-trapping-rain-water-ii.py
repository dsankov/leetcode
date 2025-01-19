class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        num_rows, num_cols = len(heightMap), len(heightMap[0])
        boundary = []
        visited_cells = [[False] * num_cols for _ in range(num_rows)]
        DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))

        for row in range(num_rows):
            boundary.append((heightMap[row][0], (row, 0)))
            visited_cells[row][0] = True
            boundary.append((heightMap[row][num_cols-1], (row, num_cols-1)))
            visited_cells[row][num_cols - 1] = True
        for col in range(num_cols):
            boundary.append((heightMap[0][col], (0, col)))
            visited_cells[0][col] = True
            boundary.append((heightMap[num_rows-1][col], (num_rows-1, col)))
            visited_cells[num_rows - 1][col] = True
        heapify(boundary)

        total_trapped = 0
        while boundary:
            min_boundary_height, (boundary_row, boundary_col) = heappop(boundary)
            for d_row, d_col in DIRECTIONS:
                new_row, new_col = boundary_row + d_row, boundary_col + d_col
                if not (0 <= new_row < num_rows and 0 <= new_col < num_cols and not visited_cells[new_row][new_col]):
                    continue
                if heightMap[new_row][new_col] < min_boundary_height:
                    total_trapped += min_boundary_height - heightMap[new_row][new_col]
                heappush(boundary,
                            (
                            max(heightMap[new_row][new_col], min_boundary_height),
                            (new_row, new_col)
                            )
                        )
                visited_cells[new_row][new_col] = True

        return total_trapped
        