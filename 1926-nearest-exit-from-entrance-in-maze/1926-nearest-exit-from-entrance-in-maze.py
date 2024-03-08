class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        EMPTY = "."
        WALL = "+"
        def is_exit(point) -> bool:
            if point == entrance:
                return False
            point_y, point_x = point
            if point_y in {0, len(maze)-1} or point_x in {0, len(maze[0])-1}:
                return True
            return False

        def get_moves(point) -> List[int]:
            result = []
            point_y, point_x = point
            directions = ((-1,0),(0,-1),(1,0),(0,1))
            for y_move, x_move in directions:
                if 0 <= point_y + y_move <= len(maze) - 1 \
                and 0 <= point_x + x_move <= len(maze[0]) - 1 \
                and maze[point_y + y_move][point_x + x_move] == EMPTY:
                    result.append((point_y + y_move,point_x + x_move))
                    
            return result
        
        moves_to_test = deque()
        moves_to_test.append((entrance, 0)) # (position, path_length)
        visited_moves = set()
        visited_moves.add(tuple(entrance))
        
        while moves_to_test:
            test_move, length_so_far = moves_to_test.popleft()
            if is_exit(test_move):
                return length_so_far
            availible_moves = get_moves(test_move)
            for move in availible_moves:
                if move not in visited_moves:
                    visited_moves.add(move)
                    moves_to_test.append((move, length_so_far + 1))

        return -1