class Solution:
    def minimumSteps(self, s: str) -> int:
        black_ball_counter = 0
        total_swaps = 0
        for i, ball in enumerate(s):
            if ball == "0":
                total_swaps += black_ball_counter
            else:
                black_ball_counter += 1
        return total_swaps
        