class Solution:
    def findComplement(self, num: int) -> int:
        return int("".join("1" if char == "0" else "0" for char in f"{num:b}"), base=2)
        