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
        
        max_length = max(
            (length 
                for (char, length), freq in filter(lambda item: item[1] >= 3, substr_freqs.items())),
            default= -1  
        )

        return max_length 


