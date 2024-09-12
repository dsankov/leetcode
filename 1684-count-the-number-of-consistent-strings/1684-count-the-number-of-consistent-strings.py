class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum(set(word) <= set(allowed) for word in words)
        