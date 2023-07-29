class Solution:
    def isPalindrome(self, s: str) -> bool:
        prepared_letters = ''.join(filter(str.isalnum, s)).lower()
        return prepared_letters == prepared_letters[::-1]