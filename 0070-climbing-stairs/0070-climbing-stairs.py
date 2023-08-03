class Solution:
    def climbStairs(self, n: int) -> int:
        number_of_ways = [0] * 46
        number_of_ways[0], number_of_ways[1] = 1, 1

        for step in range(2, n+1):
            number_of_ways[step] = number_of_ways[step-1] + number_of_ways[step-2]
            
        return number_of_ways[n]
            