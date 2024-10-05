class Solution:
    def checkInclusion(self, pattern: str, string: str) -> bool:
        pattern_len = len(pattern)
        str_len = len(string)
        if pattern_len > str_len:
            return False
        pattern_counter = Counter(pattern)
        pattern_letters = len(pattern_counter)
        matched_letters = 0
        for i in range(str_len):
            if string[i] in pattern_counter:
                pattern_counter[string[i]] -= 1
                if pattern_counter[string[i]] == 0:
                    matched_letters += 1
            if i >= pattern_len and string[i - pattern_len] in pattern_counter:
                if pattern_counter[string[i - pattern_len]] == 0:
                    matched_letters -= 1
                pattern_counter[string[i - pattern_len]] += 1
            if matched_letters == pattern_letters:
                return True
        return False
        