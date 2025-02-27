class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)

        a_count = sum(ch == "a" for ch in s)
        b_count = 0
        min_deletions = n
        for ch in s:
            if ch == "a":
                a_count -= 1
            min_deletions = min(min_deletions, a_count + b_count)
            if ch == "b":
                b_count += 1

        return min_deletions
        