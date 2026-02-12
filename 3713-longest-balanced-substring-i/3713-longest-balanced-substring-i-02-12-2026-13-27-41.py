class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 1
        for left in range(n):
            seen = defaultdict(int)
            seen[s[left]] = 1
            for right in range(left+1, n):
                seen[s[right]] += 1
                if all(seen[s[left]] == count for count in seen.values()):
                    max_len = max(max_len, right - left + 1) 
        return max_len
        