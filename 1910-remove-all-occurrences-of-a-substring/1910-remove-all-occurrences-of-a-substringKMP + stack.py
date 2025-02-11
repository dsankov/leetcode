class Solution:
    def removeOccurrences(self, s: str, pattern: str) -> str:
        pattern_len = len(pattern)
        str_len = len(s)

        def compute_lps(pattern):
            lps = [0]
            j = 0
            for i in range(1, len(pattern)):
                while j > 0 and pattern[j] != pattern[i]:
                    j = lps[j - 1]
                if pattern[j] == pattern[i]:
                    j += 1
                lps.append(j)
            return lps

        pattern_lps = compute_lps(pattern)

        char_stack = []
        char_stack.append(("", 0))
        for cur_char in s:
            _, j = char_stack[-1]
            while j > 0 and pattern[j] != cur_char:
                j = pattern_lps[j - 1]
            if pattern[j] == cur_char:
                j += 1
            char_stack.append((cur_char, j))
            if j == pattern_len:
                for _ in range(pattern_len):
                    char_stack.pop()

            
        return "".join(char for char, _ in char_stack)
       