class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1),  (1, 0),  (0, -1), (-1, 0), ]
        max_distance = 0
        obstacles = set((x, y) for x, y in obstacles)
        cur_pos = (0, 0)
        cur_dir = 0
        for command in commands:
            if command == -1:
                cur_dir = (cur_dir + 1) % 4
                continue
            elif command == -2:
                cur_dir = (cur_dir + 3) % 4
                continue

            for move in range(command):
                move_cand = (
                    cur_pos[0] + directions[cur_dir][0],
                    cur_pos[1] + directions[cur_dir][1]
                )
                if move_cand in obstacles:
                    break
                
                cur_pos = move_cand
                max_distance = max(max_distance, cur_pos[0]**2 + cur_pos[1]**2)
       
        return max_distance
        