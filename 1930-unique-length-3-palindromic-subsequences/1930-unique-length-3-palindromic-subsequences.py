class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first_occurrence = defaultdict()
        last_occurrence = defaultdict()
        for idx, letter in enumerate(s):
            if letter not in first_occurrence:
                first_occurrence[letter] = idx
            last_occurrence[letter] = idx

        result = 0
        for edge_letter in first_occurrence:
            first_idx = first_occurrence[edge_letter]
            last_idx = last_occurrence[edge_letter]
            result += len(set(s[first_idx + 1:last_idx]))

        return result