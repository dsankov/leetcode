class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if len(moves) % 2 != 0:
            return False

        move_counts = collections.Counter(moves)

        return move_counts["U"] == move_counts["D"] and move_counts["R"] == move_counts["L"]
        