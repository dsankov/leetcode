class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        ALLOWED_CHARS = "abc"
        chars_counter = Counter(s)
        if any(chars_counter[char] < k for char in ALLOWED_CHARS):
            return -1
            
        n = len(s)
        left = 0
        curr_window_chars_counter = defaultdict(int)
        max_window_size = 0
        for right in range(n):
            curr_window_chars_counter[s[right]] += 1
            while (left <= right
                   and any(chars_counter[char] - curr_window_chars_counter[char] < k
                            for char in ALLOWED_CHARS)
            ):
                curr_window_chars_counter[s[left]] -= 1
                left += 1

            max_window_size = max(max_window_size, right - left + 1)

        return n - max_window_size
        