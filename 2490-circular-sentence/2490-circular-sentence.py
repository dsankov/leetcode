class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        return all(first[-1] == next[0] for first, next in pairwise(sentence.split() * 2))
        