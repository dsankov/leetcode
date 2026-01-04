from typing import List
import math

class Solution:
    def build_sieve(self, n: int):
        sieve = [True] * (n + 1)
        sieve[0] = False
        sieve[1] = False
        p = 2
        while p * p <= n:
            if sieve[p]:
                for multiple in range(p*p, n+1, p):
                    sieve[multiple] = False
            p += 1
        return sieve

    def sumFourDivisors(self, nums: List[int]) -> int:
        max_num = max(nums)
        sieve = self.build_sieve(max_num)

        total = 0
        for x in nums:
            p = round(x ** (1/3))
            if p**3 == x and sieve[p]:
                total += 1 + p + p*p + x
                continue

            i = 2
            while i * i <= x:
                if x % i == 0:
                    j = x // i
                    if i != j and sieve[i] and sieve[j]:
                        total += 1 + i + j + x
                    break
                i += 1
        return total
