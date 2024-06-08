class Solution:
    def equalSubstring(self, s: str, t: str, max_cost: int) -> int:
        n = len(s)
        # assert n == len(t)
        differences = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]
        left, right = 0, 0
        cur_cost = 0
        max_len = 0
        
        while right <= n:
            if cur_cost > max_cost:
                cur_cost -= differences[left]
                left += 1
            else:
                max_len = max(max_len, right - left )
                if right < n:
                    cur_cost += differences[right]
                right += 1

        return max_len     