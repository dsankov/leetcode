class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        substr_freqs = collections.defaultdict(int)
        substr_count = 0
        left = right = 0
        right_letter = s[right]
        substr_freqs[right_letter] += 1
        while left < n:
            if (substr_freqs["a"] > 0
                and substr_freqs["b"] > 0
                and substr_freqs["c"] > 0
            ):
                substr_count += n - right

                left_letter = s[left]
                substr_freqs[left_letter] -= 1
                left += 1
            else:
                if right < n - 1:
                    right += 1
                    right_letter = s[right]
                    substr_freqs[right_letter] += 1
                else:
                    break
        return substr_count
