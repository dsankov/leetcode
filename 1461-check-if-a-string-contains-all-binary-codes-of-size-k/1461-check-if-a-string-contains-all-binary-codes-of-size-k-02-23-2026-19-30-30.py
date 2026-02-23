class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        substrs = set()
        for i in range(len(s) + 1 - k):
            substrs.add(s[i:i+k])
        return len(substrs) == 2 ** k
        