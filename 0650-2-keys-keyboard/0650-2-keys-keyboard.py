class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        for divider in range(2, n+1):
            if n % divider== 0:
                return divider + self.minSteps(n // divider)