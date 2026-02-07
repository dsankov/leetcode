class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        total_a = s.count("a")
        if total_a in (0, n):
            return 0
        total_b = n - total_a

        a_from_start = 0
        chars_to_del = n
        for i, char in enumerate(s):
            if char == "a":
                a_from_start += 1

            b_from_start = 1 + i - a_from_start  
            a_to_end = total_a - a_from_start
            b_to_end = total_b - b_from_start   

            chars_to_del = min(chars_to_del, b_from_start + a_to_end)

        return chars_to_del   