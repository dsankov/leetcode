class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1":
            return False
        n = len(s)
        reached = [False] * n
        reached[0] = True
        sources = 0
        last_seen = 0

        for i in range(1, n):
            if 0 <= i - minJump and reached[i - minJump]:
                sources += 1
            if 0 <= i - (maxJump + 1) and reached[i - (maxJump + 1)]:
                sources -= 1
            if s[i] == "0" and sources > 0:
                reached[i] = True
                last_seen = i
            if last_seen < i - maxJump:
                return False
        return reached[-1]
             
        