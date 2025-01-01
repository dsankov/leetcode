class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        zeroes = [0] * n
        zeroes[0] = 1 if s[0] == "0" else 0
        for i in range(1, n):
            zeroes[i] = zeroes[i-1] + (1 if s[i] == "0" else 0)

        ones = [0] * n
        ones[-1] = 1 if s[-1] == "1" else 0
        for i in range(n - 2, -1, -1):
            ones[i] = ones[i+1] + (1 if s[i] == "1" else 0)

        result = 0
        for i in range(0, n-1):
            result = max(result, zeroes[i] + ones[i+1])

        return result
