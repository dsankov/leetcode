from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_of_letters = Counter(s)
        palindrome_length = 0
        odd_number_found = False

        for letter, number_of_letter in count_of_letters.items():
            if number_of_letter % 2:
                odd_number_found = True
                palindrome_length += number_of_letter - 1
            else:
                palindrome_length += number_of_letter

        palindrome_length += odd_number_found  # False=0, True=1
        return palindrome_length
