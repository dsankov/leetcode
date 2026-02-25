class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        bits_values = [(bin(num).count("1"), num) for num in arr]
        bits_values.sort()
        return [value for bits, value in bits_values]
        