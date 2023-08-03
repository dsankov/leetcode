class Solution:
    def addBinary(self, a: str, b: str) -> str:

        extended_a = '0' * max(0, len(b)-len(a)) + a
        extended_b = '0' * max(0, len(a)-len(b)) + b
        
        binary_sum = ''
        owerflow_bit = 0
        for a_bit, b_bit in zip(map(int, extended_a[::-1]), map(int, extended_b[::-1])):
            sum_bit = (a_bit + b_bit + owerflow_bit) % 2
            owerflow_bit = (a_bit + b_bit + owerflow_bit) // 2
            binary_sum = str(sum_bit) + binary_sum
        binary_sum = ('1' if owerflow_bit else '') + binary_sum
  
        return binary_sum