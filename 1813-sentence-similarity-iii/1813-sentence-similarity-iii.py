class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sentence1 = sentence1.split()
        sentence2 = sentence2.split()
        if len(sentence1) > len(sentence2):
            sentence1, sentence2 = sentence2, sentence1
        left = 0
        right1, right2 = len(sentence1) - 1, len(sentence2) - 1
        while left < len(sentence1) and sentence1[left] == sentence2[left]:
            left += 1
        while right1 >= 0 and sentence1[right1] == sentence2[right2]:
            right1 -= 1
            right2 -= 1
        return left > right1