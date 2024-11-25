class Solution:

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        moves = {0: (1, 3),
                1: (0, 2, 4),
                2: (1, 5),
                3: (0, 4),
                4: (1, 3, 5),
                5: (2, 4),
        }

        state_queue = deque()
        visited = set()
        move_count = 0

        solved_state = "123450"
        start_state = "".join(map(str,chain.from_iterable(board)))
        state_queue.append((start_state, start_state.index("0")))
        visited.add(start_state)

        while state_queue:
            for _ in range(len(state_queue)):
                curr_state, zero_position = state_queue.popleft()
                if curr_state == solved_state:
                    return move_count

                for move in moves[zero_position]:
                    candidate_state = self.make_move(curr_state, zero_position, move)
                    if candidate_state not in visited:
                        state_queue.append((candidate_state, move))
                        visited.add(candidate_state)
            move_count += 1            

        return -1

    def make_move(self, state, zero_position, move):
        a, b = (zero_position, move) if zero_position < move else (move, zero_position)
        return state[0:a] + state[b] + state[a+1:b] + state[a] + state[b+1:]
        
        