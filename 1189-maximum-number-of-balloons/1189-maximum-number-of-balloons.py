class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        pattern_freqs = Counter("balloon")
        letter_freqs = Counter(text)
        return min(
            letter_freqs[pattern_letter] // pattern_freq
            for pattern_letter, pattern_freq in pattern_freqs.items()
        )
        
