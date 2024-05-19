class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1
        
        tribonacci_numbers = [0] * (n+1)
        tribonacci_numbers[1], tribonacci_numbers[2] = 1, 1
        for i in range (3, n+1):
            tribonacci_numbers[i] = (tribonacci_numbers[i-3] + tribonacci_numbers[i-2] + tribonacci_numbers[i-1])
        return tribonacci_numbers[n]