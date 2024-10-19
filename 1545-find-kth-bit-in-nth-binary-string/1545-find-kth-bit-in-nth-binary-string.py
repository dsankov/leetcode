class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        flip_count = 0
        lenght = (1 << n) - 1
        while k > 1:
            if k == lenght // 2 + 1:
                return str(flip_count ^ 1)
            if k > lenght // 2 + 1:
                k = lenght + 1 - k
                flip_count ^= 1
            
            lenght = lenght // 2

        return str(flip_count)
        