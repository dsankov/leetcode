class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(n, k):
            # print(f"{n=} {k=}")

            if n == 1:
                return 0

            sn_len = 2 ** n - 1
            half_len = (sn_len - 1) // 2
            
            if k <= half_len:
                # print("1st half")
                h = helper(n-1, k)
                # print(f"{n=} {h=}")
                return h
            if k == half_len + 1:
                # print("Middle", 1)
                return 1
            
            # print("2nd half")
            h = helper(n-1, half_len + 1 - (k - (half_len + 1)))
            # print(f"{n=} {h=}")
            return 1 - h

        return str(helper(n, k))
        