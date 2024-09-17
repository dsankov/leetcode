class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words_1 = Counter(s1.split())
        words_2 = Counter(s2.split())
        result = []
        for word in set(words_1) - set(words_2):
            if words_1[word] == 1:
                result.append(word) 
        for word in set(words_2) - set(words_1):
            if words_2[word] == 1:
                result.append(word) 
        return result
        