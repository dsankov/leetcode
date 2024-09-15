class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        freqs = defaultdict(lambda: -1)
        vowels_map = {
            "a": 0b00001,
            "e": 0b00010,
            "i": 0b00100,
            "o": 0b01000,
            "u": 0b10000
        }
        vowels = set(vowels_map)
        prefix_xor = 0
        max_substr_len = 0
        for i, letter in enumerate(s):
            if letter in vowels:
                prefix_xor ^= vowels_map[letter]
            if prefix_xor != 0 and freqs[prefix_xor] == -1:
                freqs[prefix_xor] = i
            max_substr_len = max(
                max_substr_len,
                i - freqs[prefix_xor]
            )
        return max_substr_len