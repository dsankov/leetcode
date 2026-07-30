class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        result = 0
     
        while n > 0:
            result += n
            n -= 8


        return result
        