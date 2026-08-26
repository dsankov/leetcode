class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        one_count = 0
        min_beaut_len = inf
        beaut_subs = set()

        left = right = 0
        while right < n:

            if s[right] == "1":
                one_count += 1
            if one_count < k:
                right += 1
                continue

            if one_count == k:
                while s[left] == "0":
                    left += 1

                if right + 1 - left < min_beaut_len:
                    min_beaut_len = right + 1 - left
                    beaut_subs = set()
                    beaut_subs.add(s[left:right + 1])
                elif right + 1 - left == min_beaut_len:
                    beaut_subs.add(s[left:right + 1])
            
            while left < right:
                if s[left] == "1":
                    one_count -= 1
                left += 1
                if one_count < k:
                    break
            right += 1


            


        return "" if not beaut_subs else min(beaut_subs)
        