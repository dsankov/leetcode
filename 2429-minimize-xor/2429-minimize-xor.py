class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        result = 0
        MAX_BITS = ceil(log2(10**9))
        bits = [0] * MAX_BITS
        xor_mask = [0] * MAX_BITS
        bits_count = 0
        for i in range(MAX_BITS):
            bits[i] = (num1 >> i) & 1
            bits_count += (num2 >> i) & 1
        for i in range(MAX_BITS - 1, -1, -1):
            if bits[i] == 1 and bits_count > 0:
                xor_mask[i] = 1
                bits_count -= 1

        for i in range(MAX_BITS):
            if bits_count == 0:
                break
            if bits[i] == 0:
                bits_count -= 1
                xor_mask[i] = 1

        for i in range(MAX_BITS):
            if xor_mask[i]:
                result += 1 << i
        return result
        