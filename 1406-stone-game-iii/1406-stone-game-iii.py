class Solution:
    def stoneGameIII(self, A: List[int]) -> str:
        n = len(A)

        @cache
        def maxDiff(i: int) -> int:
            if i == n: return 0
            a = b = c = -5e7

            if i < n:
                a = A[i] - maxDiff(i + 1)
            if i + 1 < n:
                b = A[i] + A[i + 1] - maxDiff(i + 2)
            if i + 2 < n:
                c = A[i] + A[i + 1] + A[i + 2] - maxDiff(i + 3)

            return max(a, b, c)

        d = maxDiff(0)
        if d < 0:
            return "Bob"
        elif d > 0:
            return "Alice"
        else:
            return "Tie"

        