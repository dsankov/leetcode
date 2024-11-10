class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        NUM_BITS = ceil(log2(max(a, b, c))) + 1
        a = [(a >> bit_index) & 1 for bit_index in range(NUM_BITS)]
        b = [(b >> bit_index) & 1 for bit_index in range(NUM_BITS)]
        c = [(c >> bit_index) & 1 for bit_index in range(NUM_BITS)]
        result = 0
        for bit_index in range(NUM_BITS):
            if c[bit_index] == 1:
                result += 1 - (a[bit_index] | b[bit_index])
            else:
                result += a[bit_index] + b[bit_index]
        return result 