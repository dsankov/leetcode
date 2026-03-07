class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        flips_to_01_str = flips_to_10_str = 0
        min_flips = inf

        for end in range(2 * n):
            if end % 2 == ord(s[end % n]) - ord("0"):
                flips_to_10_str += 1
            else:
                flips_to_01_str += 1
            if end >= n:
                start = end - n
                if start % 2 == ord(s[start % n]) - ord("0"):
                    flips_to_10_str -= 1
                else:
                    flips_to_01_str -= 1
                min_flips = min(min_flips, flips_to_01_str, flips_to_10_str)

        return min_flips
                
        