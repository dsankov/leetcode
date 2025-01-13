class Solution:
    def minimumLength(self, s: str) -> int:
        return sum(2 - freq % 2 for freq in Counter(s).values())
        