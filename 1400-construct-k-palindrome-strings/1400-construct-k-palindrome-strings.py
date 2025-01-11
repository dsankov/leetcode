class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        return sum(freq % 2 == 1 for _, freq in Counter(s).items()) <= k
        