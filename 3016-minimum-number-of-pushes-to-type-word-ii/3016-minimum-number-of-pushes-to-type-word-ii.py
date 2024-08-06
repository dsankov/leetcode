class Solution:
    def minimumPushes(self, word: str) -> int:
        return sum((i // 8 + 1) * freq for i, freq in enumerate(sorted(Counter(word).values(), reverse=True)))