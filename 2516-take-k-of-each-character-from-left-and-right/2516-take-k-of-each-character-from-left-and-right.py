class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        ALLOWED_CHARS = "abc"
        total_chars_counter = Counter(s)
        if any(total_chars_counter[char] < k for char in ALLOWED_CHARS):
            return -1

        n = len(s)
        left = 0
        curr_window_chars_counter = defaultdict(int)
        max_window_size = 0
        for right, char in enumerate(s):
            curr_window_chars_counter[char] += 1
            while (left <= right
                   and total_chars_counter[char] - curr_window_chars_counter[char] < k
            ):
                curr_window_chars_counter[s[left]] -= 1
                left += 1

            max_window_size = max_window_size if max_window_size > right - left + 1 else right - left + 1

        return n - max_window_size
        