class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MODULO = 10 ** 9 + 7
        result = 0

        for num in range(1, n + 1):
            result = ((result  <<  (len(bin(num) )  - 2)) + num) % MODULO

        return result
        