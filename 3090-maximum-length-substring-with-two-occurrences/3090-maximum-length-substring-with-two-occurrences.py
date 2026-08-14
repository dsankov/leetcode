class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        freqs = defaultdict(int)
        left = right = 0
        max_len = 0
        while right < n:
            freqs[s[right]] += 1
            while 2 < freqs[s[right]]:
                freqs[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len

        