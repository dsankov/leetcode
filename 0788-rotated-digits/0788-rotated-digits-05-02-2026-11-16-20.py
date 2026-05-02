class Solution:
    def rotatedDigits(self, n: int) -> int:
        return sum(
            all(d in "0125689" for d in num) and
            not all(d in "018" for d in num)     
            for num in map(str, range(n + 1))
            )
            
        