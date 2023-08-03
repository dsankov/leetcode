from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_letters = Counter(ransomNote)
        magazine_letters = Counter(magazine)
        for letter, number_of_letters in ransom_letters.items():
            if number_of_letters > magazine_letters.get(letter, 0):
                return False
        return True