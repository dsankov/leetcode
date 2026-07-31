class Solution:
    def minimumPushes(self, word: str) -> int:
        freqs = collections.Counter(word)
        result = 0
        pushes = 0
        for id, (char, freq) in enumerate(freqs.most_common()):
            if id % 8 == 0:
                pushes += 1
            result += freq * pushes

        return result