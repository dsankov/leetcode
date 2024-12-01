from pprint import pp
# "cbaebabacd"

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        pattern_freqs = Counter(p)
        pattern_letters_num = len(pattern_freqs)
        slide_freqs = Counter(s[ : m - 1 ])
        slide_letters_num = sum(slide_freqs[char] == pattern_freqs[char] for char in pattern_freqs)

        left, right = 0, m - 1
        result = []
        while right < n:
            right_char = s[right]
            if pattern_freqs[right_char] != 0 and slide_freqs[right_char] == pattern_freqs[right_char]:
                slide_letters_num -= 1 

            slide_freqs[right_char] += 1

            if slide_freqs[right_char] == pattern_freqs[right_char]:
                slide_letters_num += 1
            
            if slide_letters_num == pattern_letters_num:
                result.append(left)

            left_char = s[left]
            if pattern_freqs[left_char] != 0 and slide_freqs[left_char] == pattern_freqs[left_char]:
                slide_letters_num -= 1

            slide_freqs[left_char] -= 1
            if pattern_freqs[left_char] != 0 and slide_freqs[left_char] == pattern_freqs[left_char]:
                slide_letters_num += 1

            right += 1
            left += 1

        return result