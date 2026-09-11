class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        digits_count = Counter(str(d) for d in digits)
        result = 0
        for num in range(100, 999, 2):
            num_digits_count = Counter(str(num))
            if num_digits_count <= digits_count:
                result += 1
        return result
        