class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_counts = Counter(words)
        center_used = False
        result = 0
        for word in word_counts:
            word_count = min(word_counts[word], word_counts[word[::-1]])
            if word != word[::-1]:
                result += word_count * len(word)
            else:
                result += 2 * (word_count // 2) * len(word)
                if not center_used and word_count % 2:
                    center_used = True
                    result += len(word)
                    
        return result