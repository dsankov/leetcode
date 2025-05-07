class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n = len(moveTime)
        m = len(moveTime[0])
        visit_time = [[inf] * m for _ in range(n)]
        visited = [[False] * m for _ in range(n)]
        visit_time[0][0] = 0
        cell_queue = [(0, 0, 0)]

        while cell_queue:
            cur_time, cur_y, cur_x = heappop(cell_queue)
            if visited[cur_y][cur_x]:
                continue
            visited[cur_y][cur_x] = True

            for d_y, d_x in DIRS:
                next_y = cur_y + d_y
                next_x = cur_x + d_x
                if not (0 <= next_y < n and 0 <= next_x < m):
                    continue
                next_time = 1 + max(
                    visit_time[cur_y][cur_x], 
                    moveTime[next_y][next_x]
                    )
                if next_time < visit_time[next_y][next_x]:
                    visit_time[next_y][next_x] = next_time
                    heappush(cell_queue, (next_time, next_y, next_x)) 

        return visit_time[n - 1][m - 1]


        