class Solution:
    def sumAndMultiply(self, n: int) -> int:
        n = list(map(int, str(n)))
        sum_n = sum(n)
        x = []
        for d in n:
            if d != 0:
                x.append(str(d))
        x = int("".join(x)) if len(x) > 0 else 0
        return x * sum_n
