class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        diff_array = [0] * n  

        for start, end, direction in shifts:
            if direction == 1:
                diff_array[start] += 1
                if end < n - 1:
                    diff_array[end + 1] -= 1  
            else: 
                diff_array[start] -= 1  
                if end < n - 1:
                    diff_array[end + 1] += 1

        result = [""] * n
        number_of_shifts = 0

        for i in range(n):
            number_of_shifts = (
                number_of_shifts + diff_array[i]
            ) % 26  

            shifted_char = chr(
                (ord(s[i]) - ord("a") + number_of_shifts) % 26 + ord("a")
            )
            result[i] = shifted_char

        return "".join(result)