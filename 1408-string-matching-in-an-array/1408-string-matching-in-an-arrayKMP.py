class Solution:
    def stringMatching(self, words):
        matching_words = []

        for pattern_word_idx, pattern_word in enumerate(words):
            pattern_word_lps = self.compute_lps(pattern_word)
            for word_idx, word in enumerate(words):
                if pattern_word_idx == word_idx:
                    continue
                if self.is_substr(pattern_word, pattern_word_lps, word):
                    matching_words.append(pattern_word)
                    break 
                    
        return matching_words

    def compute_lps(self, pattern):
        lps = [0] * len(pattern)
        prefix_length = 0
        cur_idx = 1

        while cur_idx < len(pattern):
            if pattern[cur_idx] == pattern[prefix_length]:
                prefix_length += 1
                lps[cur_idx] = prefix_length
                cur_idx += 1
            else:
                if prefix_length > 0:
                    prefix_length = lps[prefix_length - 1]
                else:
                    cur_idx += 1

        return lps

    def is_substr(self, pattern, pattern_lps, text):
        pattern_idx= 0
        text_idx = 0

        while text_idx < len(text):
            if text[text_idx] == pattern[pattern_idx]:
                text_idx += 1
                pattern_idx += 1
                if pattern_idx == len(pattern):
                    return True
            else:
                if pattern_idx > 0:
                    pattern_idx = pattern_lps[pattern_idx - 1]
                else:
                    text_idx += 1
        return False