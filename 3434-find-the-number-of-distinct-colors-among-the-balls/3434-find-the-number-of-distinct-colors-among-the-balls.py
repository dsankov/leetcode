class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color = {}
        color_freqs = {}
        distinct_colors = 0
        result = []
        for ball, color in queries:
            if ball not in ball_color:
                ball_color[ball] = color

            else:
                prev_color = ball_color[ball]
                color_freqs[prev_color] -= 1
                if color_freqs[prev_color] == 0:
                    del color_freqs[prev_color]
                    distinct_colors -= 1
                ball_color[ball] = color

            if color in color_freqs:
                color_freqs[color] += 1
            else:
                color_freqs[color] = 1
                distinct_colors += 1

            result.append(distinct_colors)
        return result