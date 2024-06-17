class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c % 4 == 3:
            return False
        upper = int(c**0.5)
        lower = 0
        while lower <= upper:
            test_value = lower*lower + upper*upper 
            if test_value == c:
                return True
            if test_value < c:
                lower += 1
            else:
                upper -= 1
        return False