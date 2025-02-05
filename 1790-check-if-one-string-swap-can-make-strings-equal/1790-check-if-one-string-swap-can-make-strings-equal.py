class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff_count = 0
        diffs_1 = set()
        diffs_2 = set()
        for ch_1, ch_2 in zip(s1, s2):
            if ch_1 == ch_2:
                continue
            diff_count += 1
            if diff_count > 2:
                return False
            diffs_1.add(ch_1)
            diffs_2.add(ch_2)
        return (diff_count == 0 
                or diff_count == 2 and diffs_1 == diffs_2
        )
        