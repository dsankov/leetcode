class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        a_seen = set()
        b_seen = set()
        C = []
        for a, b in zip(A, B):
            a_seen.add(a)
            b_seen.add(b)
            C.append(len(a_seen & b_seen))
        return C
        