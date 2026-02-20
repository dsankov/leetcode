class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        n = len(s)
        l = r = 0
        segments = []
        balance = 0
        while r < n:
            if s[r] == "1":
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                segments.append("1" + self.makeLargestSpecial(s[l+1:r]) + "0")
                l = r + 1
            r += 1
        segments.sort(reverse=True)
        return "".join(segments)        