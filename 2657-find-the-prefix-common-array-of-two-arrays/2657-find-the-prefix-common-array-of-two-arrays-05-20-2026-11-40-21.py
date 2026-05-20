# class Solution:
#     def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
#         n = len(A)
#         a_seen = set()
#         b_seen = set()
#         C = []
#         for a, b in zip(A, B):
#             a_seen.add(a)
#             b_seen.add(b)
#             C.append(len(a_seen & b_seen))
#         return C
        
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seenA = set()
        seenB = set()
        res = []
        cnt = 0
        for i in range(len(A)):
            if A[i] in seenB:
                cnt += 1
            else:
                seenA.add(A[i])
            if B[i] in seenA:
                cnt += 1
            else:
                seenB.add(B[i])
            res.append(cnt)
        return res