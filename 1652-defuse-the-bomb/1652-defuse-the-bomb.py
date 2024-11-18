class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        k_sums = [0] * n
        k_sums[0] = sum(code[:abs(k)])
        for i in range(1, n):
            k_sums[i] = k_sums[i-1] - code[i-1] + code[(i+abs(k)-1) % n]
        result = [0] * n
        shift = 1 if k > 0 else k
        for i in range(n):
            result[i] = k_sums[(i + shift) % n]
        return result
        
