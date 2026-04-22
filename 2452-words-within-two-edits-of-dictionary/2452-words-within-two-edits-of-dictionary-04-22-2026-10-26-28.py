class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def less_3_diff(s1, s2):
            diffs = 0
            for ch1, ch2 in zip(s1, s2):
                if ch1 != ch2:
                    diffs += 1
                if diffs > 2:
                    return False
            return True
            
        result = []
        for query in queries:
            for word in dictionary:
                if less_3_diff(query, word):
                    result.append(query)
                    break
        return result