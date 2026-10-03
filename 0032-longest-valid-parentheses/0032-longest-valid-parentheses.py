class Solution:
    def longestValidParentheses(self, s: str) -> int:
        f, b = [0, 0], [0, 0]
        res = 0
        
        for i in range(len(s)):
            f[ord(s[i]) & 1] += 1
            if f[0] == f[1]: res = max(res, f[1] << 1)
            if f[0] < f[1]: f[0] = f[1] = 0

            b[ord(s[~i]) & 1] += 1
            if b[0] == b[1]: res = max(res, b[1] << 1)
            if b[0] > b[1]: b[0] = b[1] = 0

        return res