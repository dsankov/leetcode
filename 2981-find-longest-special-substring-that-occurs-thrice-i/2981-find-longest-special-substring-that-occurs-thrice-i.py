class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        substr_freqs = defaultdict(int)
        for start in range(n):
            first_substr_char = s[start]
            substr_length = 0
            for end in range(start, n):
                if first_substr_char != s[end]:
                    break
                substr_length += 1
                substr_freqs[(first_substr_char, substr_length)] += 1
        
        max_length = -1
        for (char, length), freq in substr_freqs.items():
            if freq >= 3:
                max_length = max(max_length, length)

        return max_length 
        # if max_length != 0 else -1


