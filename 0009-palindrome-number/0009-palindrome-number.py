class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        test_x = x
        test_position = 1
        while test_position <= x:
            test_position *= 10
        test_position //= 10
        left_aprox = 0
        right_aprox = 0
        while test_x > 0:

            
            if test_x < 10:
                return True

            left_digit = (x // test_position) % 10
            right_digit = test_x % 10


            if left_digit != right_digit:
                return False

            test_x -= right_digit

            test_x //= 10
            test_position //= 10

        return True
