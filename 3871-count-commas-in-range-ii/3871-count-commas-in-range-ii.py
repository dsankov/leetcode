class Solution:
    def countCommas(self, n: int) -> int:
        comma_level = 0
        total_commas = 0
        low_edge = 10**(3*(comma_level))
        high_edge = min(10**(3*(comma_level + 1)) - 1, n)
        while high_edge < n:

            # print(low_edge, high_edge)
            comma_level += 1
            low_edge = 10**(3*(comma_level))
            high_edge = min(10**(3*(comma_level + 1)) - 1, n)
            interval = high_edge - low_edge + 1
            total_commas += interval * comma_level

        # print(low_edge, high_edge)
        return total_commas
        