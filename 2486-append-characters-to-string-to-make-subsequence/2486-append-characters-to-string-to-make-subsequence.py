class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        source_ptr, target_ptr = 0, 0
        while target_ptr < m and source_ptr < n:
            if s[source_ptr] == t[target_ptr]:
                target_ptr += 1
            source_ptr += 1
        return m - target_ptr
            
        