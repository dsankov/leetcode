class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # dp_table = [False] * (n + 1)
        # dp_table[0] = dp_table[1] = True
        # for num in range(2, n):
        #     power_of_3 = 0
        #     while num - 3 ** power_of_3 >= 0:
        #         if              

        while n > 0:
            if n % 3 > 1:
                return False
            n //= 3
        return True        