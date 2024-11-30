class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0
        while i < n and s[i] == " ":
            i += 1
        
        result = 0
        sign = 1
        if i >= n:
            return result
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            i += 1

        while i < n and s[i] == "0":
            i += 1
        
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
            if result > 2 ** 31 - 1:
                if sign > 0:
                    return 2 ** 31 - 1
                if sign < 0 and result > 2 ** 31:
                    return - 2**31
                

        return result * sign
        