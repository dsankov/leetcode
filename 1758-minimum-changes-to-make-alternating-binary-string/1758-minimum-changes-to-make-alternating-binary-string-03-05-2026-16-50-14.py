class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        odd = n // 2
        even = n - odd

        all_ones = sum(1  for ch in s if ch == "1")
        all_zeroes = n - all_ones
        
        even_ones = sum(1  for idx, ch in enumerate(s) if ch == "1" and idx % 2 == 0)
        odd_ones = all_ones - even_ones

        even_zeroes = even - even_ones
        odd_zeroes = odd - odd_ones



        return min(
            odd_ones + even_zeroes,
            odd_zeroes + even_ones
        )
        