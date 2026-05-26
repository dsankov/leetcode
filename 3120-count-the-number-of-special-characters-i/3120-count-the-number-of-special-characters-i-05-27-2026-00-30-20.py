class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # word = set(word)
        count = 0
        seen = set()
        for ch in word:
            if ch in seen:
                continue
            if ch.swapcase() in word:
                count += 1
            seen.add(ch)
            seen.add(ch.swapcase())
        return count